"""
Módulo de descoberta de postagens no perfil.

Navega até o perfil-alvo, rola o grid de posts e captura
URLs/IDs de postagens até o limite definido.

STUB — retorna lista mock. Implementação real na Fase 2.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING

from luanny.log import get_logger
from luanny.models import AppConfig

if TYPE_CHECKING:
    from luanny.browser import BrowserSession

logger = get_logger("profile_discovery")


def discover_posts(
    session: BrowserSession,
    profile_url: str,
    config: AppConfig,
    seen_post_ids: set[str] | None = None,
) -> list[tuple[str, str]]:
    """
    Descobre postagens de um perfil do Instagram.

    Navega até o perfil, rola o grid progressivamente para
    carregar elementos dinamicamente e captura URLs de posts
    até atingir `config.max_posts` ou o fim do grid.

    Args:
        session: Sessão do browser Playwright.
        profile_url: URL completa do perfil-alvo.
        config: Configuração da aplicação.

    Returns:
        Lista de tuplas (post_id, post_url) deduplicadas.
    """
    import time
    from luanny.selectors import PROFILE_POSTS_GRID
    from luanny.browser import human_delay_sync

    logger.info(
        "discovery_iniciando",
        profile_url=profile_url,
        max_posts=config.max_posts,
    )
    logger.info(
        "discovery_orientacoes",
        msg=(
            "Discovery pode levar alguns minutos dependendo do perfil. "
            "Use Ctrl+C para interromper a execução se necessário."
        ),
    )

    page = session.page
    seen = seen_post_ids or set()

    # Navegar para o perfil
    page.goto(profile_url, wait_until="load")
    time.sleep(2.0)

    # Dispensa possíveis cookies/diálogos intermitentes
    # (herdando resiliência da Fase 1).
    from luanny.auth import _dismiss_post_login_dialogs, _dismiss_cookie_banner

    _dismiss_cookie_banner(page)
    _dismiss_post_login_dialogs(page)

    discovered_links: dict[str, str] = {}

    # Combina os seletores definidos em selectors.py
    selectors_to_try = [
        PROFILE_POSTS_GRID.primary,
        *list(PROFILE_POSTS_GRID.fallbacks),
    ]

    scroll_attempts = 0
    # Em modo incremental, pode ser necessário atravessar mais itens já vistos.
    max_scroll_attempts = max(50, config.max_posts * 8)
    last_height = 0
    consecutive_since_boundary_hits = 0

    while (
        len(discovered_links) < config.max_posts
        and scroll_attempts < max_scroll_attempts
    ):
        # Extrai os links atualmente visíveis no DOM
        found_now = 0
        dated_items_this_scroll = 0
        older_than_since_this_scroll = 0

        for selector in selectors_to_try:
            elements = page.locator(selector).all()
            for el in elements:
                try:
                    href = el.get_attribute("href")
                    if href and ("/p/" in href or "/reel/" in href):
                        # Padrão: /p/CODE/ ou /reel/CODE/
                        parts = [p for p in href.split("/") if p]

                        # Procurar por 'p' ou 'reel' na lista de partes
                        id_index = -1
                        for i, part in enumerate(parts):
                            if part in ("p", "reel"):
                                id_index = i + 1
                                break

                        if id_index > 0 and id_index < len(parts):
                            post_id = parts[id_index]
                            post_url = (
                                f"https://www.instagram.com{href}"
                                if href.startswith("/")
                                else href
                            )

                            # Em resume incremental, ignorar IDs já conhecidos
                            if post_id in seen:
                                continue

                            published_at_hint = _extract_datetime_hint(el)
                            if published_at_hint is not None:
                                dated_items_this_scroll += 1
                                if (
                                    config.since is not None
                                    and published_at_hint.date() < config.since
                                ):
                                    older_than_since_this_scroll += 1
                                    continue
                                if (
                                    config.until is not None
                                    and published_at_hint.date() > config.until
                                ):
                                    continue

                            if post_id not in discovered_links:
                                discovered_links[post_id] = post_url
                                found_now += 1
                except Exception:
                    continue

            # Se encontrou algo com este seletor,
            # não precisa tentar fallbacks nesta iteração.
            if found_now > 0:
                break

        logger.debug(
            "discovery_progress",
            encontrados_total=len(discovered_links),
            meta=config.max_posts,
            posts_vistos_anteriores=len(seen),
        )
        should_log_progress = (
            found_now > 0
            or scroll_attempts == 0
            or (scroll_attempts + 1) % 3 == 0
        )
        if should_log_progress:
            logger.info(
                "discovery_progresso",
                tentativa_scroll=scroll_attempts + 1,
                tentativas_max=max_scroll_attempts,
                encontrados_total=len(discovered_links),
                novos_nesta_tentativa=found_now,
                alvo=config.max_posts,
            )

        if config.since is not None and dated_items_this_scroll > 0:
            if older_than_since_this_scroll == dated_items_this_scroll:
                consecutive_since_boundary_hits += 1
            else:
                consecutive_since_boundary_hits = 0

            if consecutive_since_boundary_hits >= 2:
                logger.info(
                    "discovery_since_boundary_reached",
                    since=config.since,
                    encontrados_total=len(discovered_links),
                )
                break

        # Se já atingimos a meta, podemos parar
        if len(discovered_links) >= config.max_posts:
            break

        # Rolar a página para carregar mais
        # Rola até o fim da página para disparar o carregamento do grid virtual
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        human_delay_sync(1.5, 3.5)

        # O Instagram usa rolagem virtual (virtualized list).
        # Se a altura não muda
        # após rolarmos e esperarmos, provavelmente chegamos ao fim do perfil.
        current_height = page.evaluate("document.body.scrollHeight")
        if current_height == last_height and found_now == 0:
            # Tentar dar um scroll um pouco superior para forçar trigger
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            final_height = page.evaluate("document.body.scrollHeight")
            if final_height == last_height:
                logger.info(
                    "discovery_fim_perfil",
                    msg="Fim do perfil atingido.",
                )
                break

        last_height = current_height
        scroll_attempts += 1

    # Prepara o resultado, garantindo o limite exato solicitado
    result_list = list(discovered_links.items())[:config.max_posts]

    logger.info(
        "discovery_concluida",
        total_encontrado=len(result_list),
        max_posts_solicitado=config.max_posts,
        max_scroll_attempts=max_scroll_attempts,
    )

    return result_list


def _extract_datetime_hint(element: object) -> datetime | None:
    """Tenta extrair datetime ISO de um bloco de post no grid."""
    raw_value = None

    # Alguns elementos podem expor datetime diretamente.
    try:
        raw_value = element.get_attribute("datetime")
    except Exception:
        raw_value = None

    # No grid, datetime costuma estar dentro de um <time datetime="...">.
    if not raw_value:
        try:
            time_element = element.locator("time[datetime]").first
            raw_value = time_element.get_attribute("datetime")
        except Exception:
            raw_value = None

    if not raw_value:
        return None

    try:
        parsed = datetime.fromisoformat(
            str(raw_value).strip().replace("Z", "+00:00")
        )
    except ValueError:
        return None

    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)
