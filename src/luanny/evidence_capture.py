"""
Módulo de captura de evidências técnicas.

Gera screenshot, salva HTML bruto e calcula hashes SHA-256
para cada post coletado, com metadados de reprodutibilidade.
"""

from __future__ import annotations

import hashlib
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING

from luanny import __version__
from luanny.log import get_logger
from luanny.models import AppConfig, Evidence, PostRecord

if TYPE_CHECKING:
    from luanny.browser import BrowserSession

logger = get_logger("evidence_capture")


def _compute_sha256(file_path: Path) -> str:
    """Calcula o hash SHA-256 de um arquivo."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Lê em blocos para não sobrecarregar memória com arquivos enormes
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def capture_evidence(
    session: BrowserSession,
    record: PostRecord,
    config: AppConfig,
    base_output_dir: Path | None = None,
) -> None:
    """
    Captura evidências técnicas para um post coletado.

    Salva screenshot PNG, HTML bruto e calcula hashes SHA-256.
    Atualiza o campo `evidence` do PostRecord in-place.

    Args:
        session: Sessão do browser Playwright.
        record: PostRecord do post (será atualizado com evidência).
        config: Configuração da aplicação.
        base_output_dir: Diretório raiz da run atual.
    """
    if not config.capture_evidence:
        logger.debug("evidence_skipped", msg="Captura de evidência desabilitada", post_id=record.post_id)
        return

    logger.info("evidence_started", post_id=record.post_id)

    # Definir diretório de evidências para este post
    run_dir = base_output_dir if base_output_dir else Path(config.output_dir)
    post_evidence_dir = run_dir / "evidence" / record.post_id
    post_evidence_dir.mkdir(parents=True, exist_ok=True)

    screenshot_path = post_evidence_dir / "screenshot.png"
    html_path = post_evidence_dir / "page.html"

    # Garantir que a página tenha terminado eventuais animações visuais
    time.sleep(1.0)

    try:
        # Capturar Screenshot
        session.page.screenshot(path=str(screenshot_path), full_page=False)

        # Capturar HTML
        html_content = session.page.content()
        html_path.write_text(html_content, encoding="utf-8")

        # Calcular hashes
        screenshot_hash = _compute_sha256(screenshot_path)
        html_hash = _compute_sha256(html_path)

        # Atualizar Record com estrutura validada em Evidence
        # Usamos caminhos relativos ao run_dir para facilitar portabilidade do dataset exportado
        rel_screenshot = screenshot_path.relative_to(run_dir).as_posix()
        rel_html = html_path.relative_to(run_dir).as_posix()

        record.evidence = Evidence(
            post_url=record.post_url,
            profile_url=f"https://www.instagram.com/{record.profile_username}/",
            screenshot_path=rel_screenshot,
            html_path=rel_html,
            screenshot_hash=screenshot_hash,
            html_hash=html_hash,
            captured_at=datetime.now(timezone.utc),
            collector_version=__version__,
            browser_language=config.browser_language,
            viewport_size="1280x720",
        )

        logger.debug("evidence_saved", post_id=record.post_id, hash=screenshot_hash[:8])
    except Exception as e:
        logger.error("evidence_failed", post_id=record.post_id, error=str(e))
