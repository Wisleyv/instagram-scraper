"""
Testes do módulo browser — Fase 1.

Testa criação e fechamento do BrowserSession,
usando mocks do Playwright.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch, PropertyMock

import pytest

from luanny.browser import (
    BrowserSession,
    DEFAULT_VIEWPORT,
    create_browser_context,
    close_browser_context,
    save_storage_state,
    _get_storage_state_path,
    human_delay_sync,
)
from luanny.models import AppConfig


@pytest.fixture()
def mock_config() -> AppConfig:
    """Config de teste para browser."""
    return AppConfig(
        instagram_username="test_user",
        instagram_password="test_pass",
        headless=True,
        browser_language="pt-BR",
        navigation_timeout=30000,
        element_timeout=10000,
    )


@pytest.fixture()
def mock_playwright():
    """Mock completo do Playwright."""
    with patch("luanny.browser.sync_playwright") as mock_sync:
        # Configurar cadeia de mocks
        pw_instance = MagicMock()
        mock_sync.return_value.start.return_value = pw_instance

        browser = MagicMock()
        pw_instance.chromium.launch.return_value = browser

        context = MagicMock()
        browser.new_context.return_value = context

        page = MagicMock()
        context.new_page.return_value = page

        yield {
            "sync_playwright": mock_sync,
            "playwright": pw_instance,
            "browser": browser,
            "context": context,
            "page": page,
        }


class TestCreateBrowserContext:
    """Testes de criação do contexto do browser."""

    def test_cria_sessao_com_playwright(self, mock_config, mock_playwright):
        """Deve criar BrowserSession com todos os componentes."""
        session = create_browser_context(mock_config)

        assert isinstance(session, BrowserSession)
        assert session.playwright is mock_playwright["playwright"]
        assert session.browser is mock_playwright["browser"]
        assert session.context is mock_playwright["context"]
        assert session.page is mock_playwright["page"]

    def test_lanca_chromium_headless(self, mock_config, mock_playwright):
        """Deve lançar Chromium com headless=True conforme config."""
        create_browser_context(mock_config)

        mock_playwright["playwright"].chromium.launch.assert_called_once()
        call_kwargs = mock_playwright["playwright"].chromium.launch.call_args
        assert call_kwargs.kwargs["headless"] is True

    def test_lanca_chromium_headed(self, mock_config, mock_playwright):
        """Deve lançar Chromium com headless=False quando config pede headed."""
        mock_config.headless = False
        create_browser_context(mock_config)

        call_kwargs = mock_playwright["playwright"].chromium.launch.call_args
        assert call_kwargs.kwargs["headless"] is False

    def test_contexto_com_idioma_pt_br(self, mock_config, mock_playwright):
        """Deve criar contexto com locale pt-BR."""
        create_browser_context(mock_config)

        call_kwargs = mock_playwright["browser"].new_context.call_args
        assert call_kwargs.kwargs["locale"] == "pt-BR"

    def test_contexto_com_viewport_padrao(self, mock_config, mock_playwright):
        """Deve criar contexto com viewport 1280x720."""
        create_browser_context(mock_config)

        call_kwargs = mock_playwright["browser"].new_context.call_args
        assert call_kwargs.kwargs["viewport"] == DEFAULT_VIEWPORT

    def test_contexto_com_timezone_sao_paulo(self, mock_config, mock_playwright):
        """Deve configurar timezone de São Paulo."""
        create_browser_context(mock_config)

        call_kwargs = mock_playwright["browser"].new_context.call_args
        assert call_kwargs.kwargs["timezone_id"] == "America/Sao_Paulo"

    def test_configura_timeouts(self, mock_config, mock_playwright):
        """Deve configurar navigation e element timeouts no contexto."""
        create_browser_context(mock_config)

        context = mock_playwright["context"]
        context.set_default_navigation_timeout.assert_called_once_with(30000)
        context.set_default_timeout.assert_called_once_with(10000)

    def test_abre_nova_pagina(self, mock_config, mock_playwright):
        """Deve abrir uma nova página no contexto."""
        create_browser_context(mock_config)

        mock_playwright["context"].new_page.assert_called_once()


class TestCloseBrowserContext:
    """Testes de fechamento do browser."""

    def test_fecha_sessao(self, mock_config, mock_playwright):
        """Deve fechar contexto, browser e playwright em ordem."""
        session = create_browser_context(mock_config)
        close_browser_context(session)

        mock_playwright["context"].close.assert_called_once()
        mock_playwright["browser"].close.assert_called_once()
        mock_playwright["playwright"].stop.assert_called_once()

    def test_nao_fecha_duas_vezes(self, mock_config, mock_playwright):
        """Fechar duas vezes não deve chamar close novamente."""
        session = create_browser_context(mock_config)
        close_browser_context(session)
        close_browser_context(session)

        # Cada um deve ter sido chamado apenas uma vez
        assert mock_playwright["context"].close.call_count == 1
        assert mock_playwright["browser"].close.call_count == 1


class TestBrowserSession:
    """Testes do dataclass BrowserSession."""

    def test_close_tolera_erros(self, mock_config, mock_playwright):
        """Close deve tolerar erros em componentes individuais."""
        mock_playwright["context"].close.side_effect = Exception("erro no context")
        mock_playwright["browser"].close.side_effect = Exception("erro no browser")

        session = create_browser_context(mock_config)
        # Não deve levantar exceção
        session.close()

        # Todos devem ter sido tentados mesmo com erro
        mock_playwright["playwright"].stop.assert_called_once()


class TestSaveStorageState:
    """Testes de persistência de sessão."""

    def test_salva_storage_state(self, mock_config, mock_playwright):
        """Deve salvar storage_state via contexto."""
        session = create_browser_context(mock_config)
        path = save_storage_state(session.context)

        session.context.storage_state.assert_called_once()
        assert path == _get_storage_state_path()


class TestHumanDelay:
    """Testes do delay humano síncrono."""

    @patch("time.sleep")
    def test_delay_dentro_do_range(self, mock_sleep):
        """Delay deve estar entre min e max."""
        human_delay_sync(1.0, 2.0)

        mock_sleep.assert_called_once()
        delay = mock_sleep.call_args[0][0]
        assert 1.0 <= delay <= 2.0
