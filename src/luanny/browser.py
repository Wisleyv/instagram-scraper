"""
Módulo de inicialização do browser (Playwright).

Responsável por criar e gerenciar o contexto do browser com
configurações apropriadas (idioma pt-BR, viewport, user agent).

Implementação real — Fase 1.
"""

from __future__ import annotations

import asyncio
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from luanny.log import get_logger
from luanny.models import AppConfig

logger = get_logger("browser")

# Viewport padrão — evita detecção por dimensões incomuns
DEFAULT_VIEWPORT = {"width": 1280, "height": 720}

# Caminho padrão para o storage state (sessão persistida)
STORAGE_STATE_PATH = Path("storage_state.json")


@dataclass
class BrowserSession:
    """
    Encapsula uma sessão de browser Playwright.

    Mantém referências ao Playwright, Browser, BrowserContext e Page
    para gerenciamento de ciclo de vida coordenado.
    """
    playwright: Playwright
    browser: Browser
    context: BrowserContext
    page: Page
    config: AppConfig
    _closed: bool = field(default=False, init=False)

    def close(self) -> None:
        """Fecha todos os recursos do browser de forma ordenada."""
        if self._closed:
            return
        try:
            self.context.close()
            logger.debug("browser_context_fechado")
        except Exception as exc:
            logger.warning("erro_ao_fechar_context", error=str(exc))
        try:
            self.browser.close()
            logger.debug("browser_fechado")
        except Exception as exc:
            logger.warning("erro_ao_fechar_browser", error=str(exc))
        try:
            self.playwright.stop()
            logger.debug("playwright_parado")
        except Exception as exc:
            logger.warning("erro_ao_parar_playwright", error=str(exc))
        self._closed = True
        logger.info("sessão_browser_encerrada")


def create_browser_context(config: AppConfig) -> BrowserSession:
    """
    Cria e retorna uma sessão de browser Playwright configurada.

    - Lança Chromium com headless conforme config
    - Cria contexto com idioma pt-BR, viewport 1280x720
    - Carrega storage_state se existente (sessão anterior)
    - Abre uma página pronta para uso

    Args:
        config: Configuração da aplicação.

    Returns:
        BrowserSession com todos os recursos inicializados.
    """
    logger.info(
        "inicializando_browser",
        headless=config.headless,
        language=config.browser_language,
    )

    pw = sync_playwright().start()

    browser = pw.chromium.launch(
        headless=config.headless,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
        ],
    )

    # Preparar opções do contexto
    context_options: dict = {
        "viewport": DEFAULT_VIEWPORT,
        "locale": config.browser_language,
        "timezone_id": "America/Sao_Paulo",
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ),
        "extra_http_headers": {
            "Accept-Language": f"{config.browser_language},{config.browser_language.split('-')[0]};q=0.9,en;q=0.8",
        },
    }

    # Se existe storage_state salvo, reusar sessão
    storage_path = _get_storage_state_path()
    if storage_path.exists():
        logger.info("sessao_existente_encontrada", path=str(storage_path))
        context_options["storage_state"] = str(storage_path)

    context = browser.new_context(**context_options)

    # Configurar timeouts padrão
    context.set_default_navigation_timeout(config.navigation_timeout)
    context.set_default_timeout(config.element_timeout)

    page = context.new_page()

    logger.info(
        "browser_pronto",
        headless=config.headless,
        viewport=f"{DEFAULT_VIEWPORT['width']}x{DEFAULT_VIEWPORT['height']}",
        language=config.browser_language,
        sessao_reusada=storage_path.exists(),
    )

    return BrowserSession(
        playwright=pw,
        browser=browser,
        context=context,
        page=page,
        config=config,
    )


def close_browser_context(session: BrowserSession) -> None:
    """
    Fecha a sessão do browser e libera todos os recursos.

    Args:
        session: Sessão do browser a ser fechada.
    """
    session.close()


def save_storage_state(context: BrowserContext) -> Path:
    """
    Salva o estado de armazenamento (cookies, localStorage) para reuso.

    Args:
        context: Contexto do browser cujo estado será salvo.

    Returns:
        Caminho do arquivo de storage state salvo.
    """
    path = _get_storage_state_path()
    context.storage_state(path=str(path))
    logger.info("sessao_salva", path=str(path))
    return path


def _get_storage_state_path() -> Path:
    """Retorna o caminho do arquivo de storage state."""
    return STORAGE_STATE_PATH


async def human_delay(min_seconds: float = 3.0, max_seconds: float = 7.0) -> None:
    """
    Aguarda um tempo aleatório simulando comportamento humano.

    Args:
        min_seconds: Delay mínimo em segundos.
        max_seconds: Delay máximo em segundos.
    """
    delay = random.uniform(min_seconds, max_seconds)
    logger.debug("human_delay", seconds=round(delay, 2))
    await asyncio.sleep(delay)


def human_delay_sync(min_seconds: float = 3.0, max_seconds: float = 7.0) -> None:
    """
    Versão síncrona do human_delay — para uso com Playwright sync API.

    Args:
        min_seconds: Delay mínimo em segundos.
        max_seconds: Delay máximo em segundos.
    """
    import time

    delay = random.uniform(min_seconds, max_seconds)
    logger.debug("human_delay", seconds=round(delay, 2))
    time.sleep(delay)
