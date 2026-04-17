"""
Módulo de descoberta de postagens no perfil.

Navega até o perfil-alvo, rola o grid de posts e captura
URLs/IDs de postagens até o limite definido.

STUB — retorna lista mock. Implementação real na Fase 2.
"""

from __future__ import annotations

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

    page = session.page
    
    # Navegar para o perfil
    page.goto(profile_url, wait_until="load")
    time.sleep(2.0)
    
    # Dispensa possíveis cookies/diálogos intermitentes (herdando resiliência da Fase 1)
    from luanny.auth import _dismiss_post_login_dialogs, _dismiss_cookie_banner
    _dismiss_cookie_banner(page)
    _dismiss_post_login_dialogs(page)

    discovered_links: dict[str, str] = {}
    
    # Combina os seletores definidos em selectors.py
    selectors_to_try = [PROFILE_POSTS_GRID.primary] + list(PROFILE_POSTS_GRID.fallbacks)

    scroll_attempts = 0
    max_scroll_attempts = 50  # Prevenção contra loop infinito
    last_height = 0

    while len(discovered_links) < config.max_posts and scroll_attempts < max_scroll_attempts:
        # Extrai os links atualmente visíveis no DOM
        found_now = 0
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
                            post_url = f"https://www.instagram.com{href}" if href.startswith("/") else href
                            if post_id not in discovered_links:
                                discovered_links[post_id] = post_url
                                found_now += 1
                except Exception:
                    continue
            
            # Se encontrou algo com este seletor, não precisa tentar os fallbacks nesta iteração
            if found_now > 0:
                break
        
        logger.debug(
            "discovery_progress", 
            encontrados_total=len(discovered_links), 
            meta=config.max_posts
        )

        # Se já atingimos a meta, podemos parar
        if len(discovered_links) >= config.max_posts:
            break

        # Rolar a página para carregar mais
        new_height = page.evaluate("document.body.scrollHeight")
        
        # Rola até o fim da página para disparar o carregamento do grid virtual
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        human_delay_sync(1.5, 3.5)
        
        # O Instagram usa rolagem virtual (virtualized list). Se a altura não muda
        # após rolarmos e esperarmos, provavelmente chegamos ao fim do perfil.
        current_height = page.evaluate("document.body.scrollHeight")
        if current_height == last_height and found_now == 0:
            # Tentar dar um scroll um pouco superior para forçar trigger
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            final_height = page.evaluate("document.body.scrollHeight")
            if final_height == last_height:
                logger.info("discovery_fim_perfil", msg="Fim do perfil atingido.")
                break
        
        last_height = current_height
        scroll_attempts += 1

    # Prepara o resultado, garantindo o limite exato solicitado
    result_list = list(discovered_links.items())[:config.max_posts]
    
    logger.info(
        "discovery_concluida",
        total_encontrado=len(result_list),
        max_posts_solicitado=config.max_posts
    )
    
    return result_list
