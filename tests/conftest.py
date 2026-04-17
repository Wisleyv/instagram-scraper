"""
Configuração compartilhada de fixtures para testes.
"""

from __future__ import annotations

import os

import pytest

from luanny.models import AppConfig


@pytest.fixture()
def mock_config() -> AppConfig:
    """Retorna uma AppConfig válida para testes, sem depender de .env real."""
    return AppConfig(
        instagram_username="test_user",
        instagram_password="test_password",
        max_posts=5,
        headless=True,
        capture_evidence=True,
        browser_language="pt-BR",
        output_dir="test_output",
    )


@pytest.fixture()
def env_with_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    """Configura variáveis de ambiente com credenciais de teste."""
    monkeypatch.setenv("INSTAGRAM_USERNAME", "test_user")
    monkeypatch.setenv("INSTAGRAM_PASSWORD", "test_password")


@pytest.fixture()
def env_without_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    """Remove variáveis de ambiente de credenciais."""
    monkeypatch.delenv("INSTAGRAM_USERNAME", raising=False)
    monkeypatch.delenv("INSTAGRAM_PASSWORD", raising=False)
