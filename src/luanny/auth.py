"""
Módulo de autenticação do Instagram.

Gerencia login, persistência de sessão (storage_state) e
detecção de checkpoints/2FA.

Implementação real — Fase 1.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING

from luanny.browser import save_storage_state, _get_storage_state_path, human_delay_sync
from luanny.log import get_logger
from luanny.models import AppConfig

if TYPE_CHECKING:
    from luanny.browser import BrowserSession

logger = get_logger("auth")

# URLs do Instagram relevantes para autenticação
INSTAGRAM_LOGIN_URL = "https://www.instagram.com/accounts/login/"
INSTAGRAM_HOME_URL = "https://www.instagram.com/"

# Seletores de login — com fallbacks para ambas as convenções de nome do Instagram
LOGIN_USERNAME_SELECTORS = [
    'input[name="username"]',                     # Convenção antiga
    'input[name="email"]',                        # Convenção atual (2025+)
    'input[autocomplete="username"]',             # Fallback por autocomplete
]
LOGIN_PASSWORD_SELECTORS = [
    'input[name="password"]',                     # Convenção antiga
    'input[name="pass"]',                         # Convenção atual (2025+)
    'input[type="password"]',                     # Fallback genérico
]
LOGIN_SUBMIT_SELECTORS = [
    'button[type="submit"]',                      # Convenção padrão
    '[role="button"][aria-label="Entrar"]',        # pt-BR via aria-label
    '[role="button"][aria-label="Log in"]',        # en via aria-label
    '[role="button"][aria-label="Log In"]',        # en alternativo
]

# Indicadores de estado pós-login
LOGGED_IN_INDICATORS = [
    'svg[aria-label="Página inicial"]',          # pt-BR: ícone Home
    'svg[aria-label="Home"]',                     # en: ícone Home (fallback)
    'a[href="/direct/inbox/"]',                   # Link do Direct
    'svg[aria-label="Pesquisa"]',                 # pt-BR: ícone Search
    'svg[aria-label="Search"]',                   # en: ícone Search (fallback)
]

# Indicadores de checkpoint/desafio
CHECKPOINT_INDICATORS = [
    'input[name="verificationCode"]',             # Campo de código 2FA
    'input[name="security_code"]',                # Código de segurança
    '#verificationCodeDescription',               # Descrição do código
    'form[data-testid="two_factor_form"]',        # Formulário 2FA
]

# Indicadores de bloqueio ou atividade suspeita
BLOCK_INDICATORS = [
    'text="Atividade suspeita"',
    'text="Suspicious activity"',
    'text="challenge_required"',
    'text="Please wait"',
    'text="Aguarde"',
]


def ensure_authenticated(session: BrowserSession, config: AppConfig) -> bool:
    """
    Garante que o browser está autenticado no Instagram.

    Fluxo:
    1. Se existe storage_state e sessão é válida → reusar
    2. Se sessão inválida ou inexistente → fazer login
    3. Se checkpoint/2FA → pausar para resolução manual

    Args:
        session: Sessão do browser Playwright.
        config: Configuração da aplicação.

    Returns:
        True se autenticação bem-sucedida.

    Raises:
        SystemExit: Se autenticação falhar irrecuperavelmente.
    """
    logger.info("auth_iniciando", username=config.instagram_username)

    # Tenta reusar sessão existente
    if _load_session(session):
        logger.info("sessao_reusada", username=config.instagram_username)
        return True

    # Sessão inválida ou inexistente — fazer login
    logger.info("login_necessario", msg="Sessão expirada ou inexistente, realizando login")
    if _perform_login(session, config):
        logger.info("login_sucesso", username=config.instagram_username)
        return True

    # Login falhou
    logger.error("login_falhou", username=config.instagram_username)
    raise SystemExit(
        "\n╔════════════════════════════════════════════════════════════╗"
        "\n║  ERRO: Não foi possível autenticar no Instagram.          ║"
        "\n║                                                            ║"
        "\n║  Possíveis causas:                                        ║"
        "\n║    • Credenciais incorretas no .env                       ║"
        "\n║    • Conta bloqueada ou com restrição                      ║"
        "\n║    • Checkpoint/2FA não resolvido                          ║"
        "\n║                                                            ║"
        "\n║  Tente executar com --headed para resolver manualmente.    ║"
        "\n╚════════════════════════════════════════════════════════════╝"
    )

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from playwright.sync_api import Error as PlaywrightError

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1.5, min=2, max=10),
    retry=retry_if_exception_type(PlaywrightError),
    reraise=True
)
def _load_session(session: BrowserSession) -> bool:
    """
    Tenta carregar e validar sessão salva.

    Navega até a home do Instagram e verifica se o usuário
    está logado (procurando indicadores de sessão ativa).

    Returns:
        True se sessão é válida e usuário está logado.
    """
    storage_path = _get_storage_state_path()
    if not storage_path.exists():
        logger.debug("sessao_inexistente", msg="Nenhum storage_state.json encontrado")
        return False

    logger.debug("validando_sessao", path=str(storage_path))

    try:
        page = session.page
        page.goto(INSTAGRAM_HOME_URL, wait_until="domcontentloaded")

        # Esperar um pouco para o conteúdo dinâmico carregar
        time.sleep(2)
        
        # (5.5) Detecção de Block logo após carregamento da sessão salva
        if _detect_block(page):
            logger.error("sessao_bloqueada", msg="A sessão guardada parece estar bloqueada pela Meta.")
            return False

        # Verificar se algum indicador de login está presente
        for selector in LOGGED_IN_INDICATORS:
            try:
                element = page.query_selector(selector)
                if element:
                    logger.debug("sessao_validada", indicador=selector)
                    return True
            except Exception:
                continue

        # Verificar se fomos redirecionados para a página de login
        if "/accounts/login" in page.url:
            logger.info("sessao_expirada", msg="Redirecionado para página de login")
            # Deletar storage_state inválido
            _invalidate_session()
            return False

        logger.info("sessao_invalida", msg="Nenhum indicador de login encontrado", url=page.url)
        return False

    except Exception as exc:
        logger.warning("erro_validacao_sessao", error=str(exc))
        return False


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1.5, min=2, max=10),
    retry=retry_if_exception_type(PlaywrightError),
    reraise=True
)
def _perform_login(session: BrowserSession, config: AppConfig) -> bool:
    """
    Realiza login no Instagram com credenciais.

    1. Navega para a página de login
    2. Preenche username e password
    3. Submete o formulário
    4. Aguarda resultado (sucesso, checkpoint, ou falha)
    5. Se sucesso, salva storage_state

    Returns:
        True se login bem-sucedido.
    """
    page = session.page

    try:
        # Navegar para página de login
        logger.debug("navegando_login_page")
        page.goto(INSTAGRAM_LOGIN_URL, wait_until="load")

        # Aguardar a página renderizar conteúdo inicial
        time.sleep(3)

        # Aceitar cookies se houver banner (comum em primeira visita)
        # Deve ser feito ANTES de esperar o formulário de login,
        # pois o banner pode cobrir/bloquear os campos.
        _dismiss_cookie_banner(page)

        # Aguardar o formulário de login aparecer (tenta cada seletor)
        logger.debug("aguardando_formulario")
        username_selector = _wait_for_any_selector(page, LOGIN_USERNAME_SELECTORS, config.navigation_timeout)
        if not username_selector:
            logger.error("formulario_nao_encontrado", msg="Nenhum campo de username encontrado")
            return False

        # Pequeno delay antes de interagir (simular comportamento humano)
        human_delay_sync(1.0, 2.0)

        # Preencher username
        logger.debug("preenchendo_username", selector=username_selector)
        username_field = page.locator(username_selector)
        username_field.click()
        username_field.fill(config.instagram_username)

        human_delay_sync(0.5, 1.0)

        # Preencher password
        password_selector = _find_first_visible(page, LOGIN_PASSWORD_SELECTORS)
        if not password_selector:
            logger.error("campo_password_nao_encontrado")
            return False
        logger.debug("preenchendo_password", selector=password_selector)
        password_field = page.locator(password_selector)
        password_field.click()
        password_field.fill(config.instagram_password)

        human_delay_sync(0.5, 1.5)

        # Submeter formulário
        submit_selector = _find_first_visible(page, LOGIN_SUBMIT_SELECTORS)
        if not submit_selector:
            logger.error("botao_submit_nao_encontrado")
            return False
        logger.debug("submetendo_login", selector=submit_selector)
        submit_btn = page.locator(submit_selector)
        submit_btn.click()

        # Aguardar resposta — múltiplos cenários possíveis
        logger.debug("aguardando_resposta_login")
        time.sleep(5)  # Esperar redirecionamento/resposta

        # Verificar se há checkpoint/2FA
        if _detect_checkpoint(page):
            _handle_checkpoint(session)
            # Após resolução do checkpoint, verificar se login foi bem-sucedido
            if _is_logged_in(page):
                save_storage_state(session.context)
                return True
            return False

        # Verificar se há bloqueio
        if _detect_block(page):
            logger.error(
                "conta_bloqueada",
                msg="Instagram detectou atividade suspeita. Tente novamente mais tarde.",
                url=page.url,
            )
            return False

        # Verificar se login foi bem-sucedido
        if _is_logged_in(page):
            # Dispensar diálogos pós-login (notificações, etc.)
            _dismiss_post_login_dialogs(page)
            save_storage_state(session.context)
            return True

        # Verificar se há erro de credenciais
        error_text = page.query_selector(
            'div[data-testid="login-error-message"], '
            '#slfErrorAlert, '
            'p[data-testid="login-error-message"]'
        )
        if error_text:
            logger.error(
                "credenciais_invalidas",
                msg=error_text.inner_text(),
            )
            return False

        # Estado desconhecido — tentar mais uma vez verificar login
        time.sleep(3)
        if _is_logged_in(page):
            _dismiss_post_login_dialogs(page)
            save_storage_state(session.context)
            return True

        logger.warning(
            "estado_login_desconhecido",
            url=page.url,
            msg="Não foi possível confirmar o resultado do login",
        )
        return False

    except Exception as exc:
        logger.error("erro_login", error=str(exc), error_type=type(exc).__name__)
        return False


def _is_logged_in(page) -> bool:
    """Verifica se a página atual indica que o usuário está logado."""
    # Verificar URL — após login, redireciona para home
    if page.url.rstrip("/") == INSTAGRAM_HOME_URL.rstrip("/") or "/accounts/login" not in page.url:
        for selector in LOGGED_IN_INDICATORS:
            try:
                element = page.query_selector(selector)
                if element:
                    return True
            except Exception:
                continue
    return False


def _detect_checkpoint(page) -> bool:
    """Detecta se a página mostra um checkpoint/desafio 2FA."""
    for selector in CHECKPOINT_INDICATORS:
        try:
            element = page.query_selector(selector)
            if element:
                logger.info("checkpoint_detectado", indicador=selector)
                return True
        except Exception:
            continue
    # Verificar pela URL
    if "challenge" in page.url or "two_factor" in page.url:
        logger.info("checkpoint_detectado_url", url=page.url)
        return True
    return False


def _detect_block(page) -> bool:
    """Detecta se o Instagram bloqueou a conta ou exige espera."""
    for indicator in BLOCK_INDICATORS:
        try:
            element = page.query_selector(indicator)
            if element:
                logger.warning("bloqueio_detectado", indicador=indicator)
                return True
        except Exception:
            continue
    return False


def _handle_checkpoint(session: BrowserSession) -> None:
    """
    Trata checkpoint/2FA no modo headed.

    Se o browser está em modo headed, pausa a execução e instrui
    o usuário a resolver o checkpoint manualmente.
    Se está em modo headless, falha com mensagem orientando uso de --headed.
    """
    if session.config.headless:
        logger.error(
            "checkpoint_headless",
            msg="Checkpoint/2FA detectado em modo headless. "
                "Execute com --headed para resolver manualmente.",
        )
        print(
            "\n╔════════════════════════════════════════════════════════════╗"
            "\n║  CHECKPOINT/2FA DETECTADO                                 ║"
            "\n║                                                            ║"
            "\n║  O Instagram solicitou verificação de segurança.          ║"
            "\n║  Execute novamente com --headed para resolver:            ║"
            "\n║                                                            ║"
            "\n║    python -m luanny scrape --profile govbr --headed        ║"
            "\n╚════════════════════════════════════════════════════════════╝"
        )
        return

    # Modo headed — pausar para resolução manual
    logger.info(
        "checkpoint_aguardando",
        msg="Resolva o checkpoint/2FA manualmente na janela do browser",
    )
    print(
        "\n╔════════════════════════════════════════════════════════════╗"
        "\n║  CHECKPOINT/2FA DETECTADO                                 ║"
        "\n║                                                            ║"
        "\n║  O Instagram solicitou verificação de segurança.          ║"
        "\n║  Resolva o desafio manualmente na janela do browser.      ║"
        "\n║                                                            ║"
        "\n║  Após resolver, pressione ENTER aqui para continuar...    ║"
        "\n╚════════════════════════════════════════════════════════════╝"
    )
    input("\n  ▸ Pressione ENTER após resolver o checkpoint... ")
    logger.info("checkpoint_resolvido_pelo_usuario")

    # Aguardar reação do Instagram após resolução
    time.sleep(3)


def _dismiss_cookie_banner(page) -> None:
    """Tenta dispensar banners de cookies/GDPR se presentes."""
    cookie_selectors = [
        'button:has-text("Aceitar")',
        'button:has-text("Accept")',
        'button:has-text("Allow")',
        'button:has-text("Permitir")',
        'button:has-text("Allow essential and optional cookies")',
        'button:has-text("Permitir cookies essenciais e opcionais")',
    ]
    for selector in cookie_selectors:
        try:
            btn = page.query_selector(selector)
            if btn and btn.is_visible():
                btn.click()
                logger.debug("cookie_banner_dispensado", selector=selector)
                time.sleep(1)
                return
        except Exception:
            continue


def _dismiss_post_login_dialogs(page) -> None:
    """
    Tenta dispensar diálogos pós-login (notificações, "salvar informações", etc.).
    """
    dismiss_selectors = [
        # "Salvar suas informações de login?" → "Agora não"
        'button:has-text("Agora não")',
        'button:has-text("Not Now")',
        # "Ativar notificações?" → "Agora não"
        'button:has-text("Agora não")',
        'button:has-text("Not now")',
        # Botão genérico de dismiss
        'button[class*="dismiss"]',
    ]

    for _ in range(3):  # Pode haver múltiplos diálogos sequenciais
        dismissed = False
        for selector in dismiss_selectors:
            try:
                btn = page.query_selector(selector)
                if btn and btn.is_visible():
                    btn.click()
                    logger.debug("dialogo_dispensado", selector=selector)
                    dismissed = True
                    time.sleep(1.5)
                    break
            except Exception:
                continue
        if not dismissed:
            break


def _invalidate_session() -> None:
    """Remove o arquivo de storage_state para forçar novo login."""
    path = _get_storage_state_path()
    if path.exists():
        path.unlink()
        logger.info("sessao_invalidada", path=str(path))


def _wait_for_any_selector(page, selectors: list[str], timeout: int) -> str | None:
    """
    Aguarda até que qualquer um dos seletores esteja visível na página.

    Usa polling rápido para verificar cada seletor em rodízio.

    Args:
        page: Página Playwright.
        selectors: Lista de seletores CSS para tentar.
        timeout: Timeout total em milissegundos.

    Returns:
        O seletor que foi encontrado, ou None se timeout expirou.
    """
    import time as _time

    deadline = _time.monotonic() + (timeout / 1000.0)

    while _time.monotonic() < deadline:
        for selector in selectors:
            try:
                element = page.query_selector(selector)
                if element and element.is_visible():
                    logger.debug("seletor_encontrado", selector=selector)
                    return selector
            except Exception:
                continue
        _time.sleep(0.5)

    logger.warning(
        "nenhum_seletor_encontrado",
        selectors=selectors,
        timeout_ms=timeout,
    )
    return None


def _find_first_visible(page, selectors: list[str]) -> str | None:
    """
    Retorna o primeiro seletor visível na página.

    Args:
        page: Página Playwright.
        selectors: Lista de seletores CSS para tentar.

    Returns:
        O primeiro seletor visível, ou None se nenhum encontrado.
    """
    for selector in selectors:
        try:
            element = page.query_selector(selector)
            if element and element.is_visible():
                return selector
        except Exception:
            continue
    return None

