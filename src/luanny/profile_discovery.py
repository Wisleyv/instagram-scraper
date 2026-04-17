"""
Módulo de descoberta de postagens no perfil.

Navega até o perfil-alvo, rola o grid de posts e captura
URLs/IDs de postagens até o limite definido.

STUB — Fase 0: retorna lista mock. Implementação real na Fase 2.
"""

from __future__ import annotations

from typing import Any

from luanny.log import get_logger
from luanny.models import AppConfig

logger = get_logger("profile_discovery")


def discover_posts(
    browser_context: Any,
    profile_url: str,
    config: AppConfig,
) -> list[tuple[str, str]]:
    """
    Descobre postagens de um perfil do Instagram.

    Navega até o perfil, rola o grid e captura URLs de posts.

    Args:
        browser_context: Contexto do browser Playwright.
        profile_url: URL completa do perfil-alvo.
        config: Configuração da aplicação.

    Returns:
        Lista de tuplas (post_id, post_url) deduplicadas.
    """
    logger.info(
        "discovery_stub",
        msg="Descoberta de posts simulada (stub)",
        profile_url=profile_url,
        max_posts=config.max_posts,
    )

    # Fase 0: retorna posts fictícios para testar o pipeline
    mock_posts = []
    for i in range(min(config.max_posts, 3)):
        post_id = f"STUB_POST_{i + 1}"
        post_url = f"https://www.instagram.com/p/{post_id}/"
        mock_posts.append((post_id, post_url))

    logger.info("discovery_stub", posts_encontrados=len(mock_posts))
    return mock_posts
