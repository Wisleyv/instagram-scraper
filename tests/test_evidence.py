"""
Testes do módulo evidence_capture — Fase 4.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from luanny.evidence_capture import _compute_sha256, capture_evidence
from luanny.models import AppConfig, PostRecord


def test_compute_sha256(tmp_path: Path):
    """Verifica se o hash SHA-256 é gerado corretamente."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("Luanny", encoding="utf-8")
    
    # sha256 de "Luanny"
    hash_valor = _compute_sha256(test_file)
    assert hash_valor == "aebee16e7988ef3ddcfa448ecf798e5afaa994b2099d1b2f493b10751387d015"


def test_capture_evidence_toggles_off(tmp_path: Path):
    """Verifica se a captura respeita o config.capture_evidence = False"""
    config = AppConfig(
        instagram_username="user",
        instagram_password="pwd",
        capture_evidence=False, # <-- Desligado
    )
    record = PostRecord(
        post_id="P1",
        post_url="url",
        profile_username="gov",
    )
    
    # Não deve gerar nada
    capture_evidence(MagicMock(), record, config, base_output_dir=tmp_path)
    
    assert record.evidence is None
    assert not (tmp_path / "evidence").exists()


def test_capture_evidence_success(tmp_path: Path):
    """Simula a captura de evidências via Playwright com mock."""
    config = AppConfig(
        instagram_username="user",
        instagram_password="pwd",
        capture_evidence=True,
    )
    record = PostRecord(
        post_id="P_MAGIC_123",
        post_url="url",
        profile_username="gov",
    )
    
    # Mock da sessão e página
    session = MagicMock()
    # Quando o screenshot rodar, vamos forçar ele a escrever um arquivo (pra simular o browser)
    def mock_screenshot(path, **kwargs):
        Path(path).write_bytes(b"fake_image_data")
        
    session.page.screenshot.side_effect = mock_screenshot
    session.page.content.return_value = "<html>mock</html>"
    
    capture_evidence(session, record, config, base_output_dir=tmp_path)
    
    # Verificações
    assert record.evidence is not None
    assert "screenshot.png" in record.evidence.screenshot_path
    assert "page.html" in record.evidence.html_path
    assert len(record.evidence.screenshot_hash) == 64
    assert len(record.evidence.html_hash) == 64
    assert record.evidence.post_url == "url"
