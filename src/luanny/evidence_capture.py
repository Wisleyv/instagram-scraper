"""
Módulo de captura de evidências técnicas.

Gera screenshot, salva HTML bruto e calcula hashes SHA-256
para cada post coletado, com metadados de reprodutibilidade.

STUB — Fase 0: simula captura. Implementação real na Fase 4.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from luanny import __version__
from luanny.log import get_logger
from luanny.models import AppConfig, Evidence, PostRecord

logger = get_logger("evidence_capture")


def capture_evidence(
    browser_context: Any,
    record: PostRecord,
    config: AppConfig,
) -> None:
    """
    Captura evidências técnicas para um post coletado.

    Salva screenshot PNG, HTML bruto e calcula hashes SHA-256.
    Atualiza o campo `evidence` do PostRecord in-place.

    Args:
        browser_context: Contexto do browser Playwright.
        record: PostRecord do post (será atualizado com evidência).
        config: Configuração da aplicação.
    """
    logger.info("evidence_stub", msg="Captura de evidência simulada (stub)", post_id=record.post_id)

    # Fase 0: preenche com dados stub
    record.evidence = Evidence(
        post_url=record.post_url,
        profile_url=f"https://www.instagram.com/{record.profile_username}/",
        screenshot_path=f"evidence/{record.post_id}/screenshot.png",
        html_path=f"evidence/{record.post_id}/page.html",
        screenshot_hash="stub_sha256_screenshot",
        html_hash="stub_sha256_html",
        captured_at=datetime.now(timezone.utc),
        collector_version=__version__,
        browser_language=config.browser_language,
        viewport_size="1280x720",
    )
