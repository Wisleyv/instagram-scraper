"""
Módulo de extração de dados do post.

Abre cada post em sua própria página e extrai todos os dados
de acessibilidade previstos no schema PostRecord.

STUB — Fase 0: retorna PostRecord mock. Implementação real na Fase 3.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from luanny.log import get_logger
from luanny.models import (
    AltTextSource,
    AppConfig,
    MediaItem,
    MediaType,
    PostRecord,
    PostType,
)

logger = get_logger("post_extractor")


def extract_post(
    browser_context: Any,
    post_id: str,
    post_url: str,
    profile_username: str,
    config: AppConfig,
) -> PostRecord:
    """
    Extrai dados de acessibilidade de um post individual.

    Abre a página do post, extrai caption, mídia, alt text,
    ARIA labels e sinais de acessibilidade.

    Args:
        browser_context: Contexto do browser Playwright.
        post_id: ID do post no Instagram.
        post_url: URL canônica do post.
        profile_username: Username do perfil-alvo.
        config: Configuração da aplicação.

    Returns:
        PostRecord com todos os dados extraídos (ou parciais em caso de erro).
    """
    logger.info("extractor_stub", msg="Extração simulada (stub)", post_id=post_id)

    # Fase 0: retorna dados fictícios para testar serialização e pipeline
    return PostRecord(
        post_id=post_id,
        post_url=post_url,
        profile_username=profile_username,
        scraped_at=datetime.now(timezone.utc),
        caption="[stub] Legenda simulada para testes do pipeline.",
        hashtags=["#stub", "#acessibilidade"],
        mentions=[],
        post_type=PostType.IMAGE,
        is_video=False,
        is_carousel=False,
        media=[
            MediaItem(
                media_index=0,
                media_type=MediaType.IMAGE,
                alt_text="[stub] Texto alternativo simulado",
                alt_text_source=AltTextSource.MANUAL,
                is_auto_generated_alt=False,
            ),
        ],
    )
