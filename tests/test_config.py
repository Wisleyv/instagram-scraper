"""
Testes do módulo de configuração — valida carregamento de .env,
overrides da CLI, e falha clara quando credenciais ausentes.
"""

from __future__ import annotations

import pytest

from luanny.config import load_config


class TestLoadConfig:
    """Testes de carregamento de configuração."""

    def test_load_config_with_env_credentials(
        self, env_with_credentials: None
    ) -> None:
        """Configuração carrega quando credenciais estão no ambiente."""
        config = load_config()
        assert config.instagram_username == "test_user"
        assert config.instagram_password == "test_password"
        assert config.max_posts == 30  # default
        assert config.browser_language == "pt-BR"  # default

    def test_load_config_fails_without_credentials(
        self, env_without_credentials: None, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Configuração falha cedo e claramente sem credenciais."""
        from unittest.mock import patch

        # Evitar que o .env real seja carregado
        with patch("luanny.config._find_env_file", return_value=None):
            with pytest.raises(SystemExit) as exc_info:
                load_config()
            assert exc_info.value.code == 1

    def test_load_config_with_cli_overrides(
        self, env_with_credentials: None
    ) -> None:
        """Overrides da CLI têm prioridade sobre .env."""
        config = load_config(max_posts=50, headless=False, output_dir="custom_output")
        assert config.max_posts == 50
        assert config.headless is False
        assert config.output_dir == "custom_output"
        # Credenciais ainda vêm do env
        assert config.instagram_username == "test_user"

    def test_load_config_env_overrides(
        self, monkeypatch: pytest.MonkeyPatch, env_with_credentials: None
    ) -> None:
        """Variáveis de ambiente opcionais são respeitadas."""
        monkeypatch.setenv("MAX_POSTS", "42")
        monkeypatch.setenv("HEADLESS", "false")
        monkeypatch.setenv("BROWSER_LANGUAGE", "pt-BR")

        config = load_config()
        assert config.max_posts == 42
        assert config.headless is False
        assert config.browser_language == "pt-BR"

    def test_cli_override_beats_env(
        self, monkeypatch: pytest.MonkeyPatch, env_with_credentials: None
    ) -> None:
        """Override explícito da CLI prevalece sobre variável de ambiente."""
        monkeypatch.setenv("MAX_POSTS", "42")
        config = load_config(max_posts=10)
        assert config.max_posts == 10

    def test_invalid_env_value_uses_default(
        self, monkeypatch: pytest.MonkeyPatch, env_with_credentials: None
    ) -> None:
        """Valor inválido no .env usa o default sem quebrar."""
        monkeypatch.setenv("MAX_POSTS", "not_a_number")
        config = load_config()
        assert config.max_posts == 30  # default
