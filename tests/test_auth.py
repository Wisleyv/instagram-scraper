"""
Testes do módulo auth — Fase 1.

Testa fluxo de autenticação, reuso de sessão, detecção de
checkpoint e tratamento de bloqueio, usando mocks do Playwright.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch, PropertyMock

import pytest

from luanny.auth import (
    ensure_authenticated,
    _load_session,
    _perform_login,
    _is_logged_in,
    _detect_checkpoint,
    _detect_block,
    _dismiss_cookie_banner,
    _dismiss_post_login_dialogs,
    _invalidate_session,
    BLOCK_INDICATORS,
    LOGGED_IN_INDICATORS,
    INSTAGRAM_LOGIN_URL,
    INSTAGRAM_HOME_URL,
    LOGIN_USERNAME_SELECTORS,
    LOGIN_PASSWORD_SELECTORS,
    LOGIN_SUBMIT_SELECTORS,
)
from luanny.browser import BrowserSession
from luanny.models import AppConfig


@pytest.fixture()
def mock_config() -> AppConfig:
    """Config de teste para auth."""
    return AppConfig(
        instagram_username="test_user",
        instagram_password="test_pass",
        headless=True,
        browser_language="pt-BR",
        navigation_timeout=30000,
        element_timeout=10000,
    )


@pytest.fixture()
def mock_session(mock_config):
    """Cria um BrowserSession mockado."""
    session = MagicMock(spec=BrowserSession)
    session.config = mock_config
    session.page = MagicMock()
    session.context = MagicMock()
    return session


class TestLoadSession:
    """Testes de carregamento de sessão salva."""

    @patch("luanny.auth._get_storage_state_path")
    def test_retorna_false_sem_storage_state(self, mock_path, mock_session):
        """Deve retornar False se não existe arquivo de sessão."""
        mock_path.return_value = MagicMock()
        mock_path.return_value.exists.return_value = False

        assert _load_session(mock_session) is False

    @patch("luanny.auth._get_storage_state_path")
    def test_retorna_true_com_sessao_valida(self, mock_path, mock_session):
        """Deve retornar True se sessão existe e indicador de login é encontrado."""
        mock_path.return_value = MagicMock()
        mock_path.return_value.exists.return_value = True

        # Simular que a página tem um indicador de login
        mock_session.page.url = INSTAGRAM_HOME_URL
        element = MagicMock()

        def fake_query_selector(selector):
            if selector in BLOCK_INDICATORS:
                return None
            if selector in LOGGED_IN_INDICATORS:
                return element
            return None

        mock_session.page.query_selector.side_effect = fake_query_selector

        assert _load_session(mock_session) is True

    @patch("luanny.auth._invalidate_session")
    @patch("luanny.auth._get_storage_state_path")
    def test_retorna_false_se_redirecionado_para_login(self, mock_path, mock_invalidate, mock_session):
        """Deve retornar False e invalidar sessão se redirecionado para login."""
        mock_path.return_value = MagicMock()
        mock_path.return_value.exists.return_value = True

        mock_session.page.url = INSTAGRAM_LOGIN_URL
        mock_session.page.query_selector.return_value = None

        assert _load_session(mock_session) is False


class TestPerformLogin:
    """Testes do fluxo de login."""

    @patch("luanny.auth.save_storage_state")
    @patch("luanny.auth._dismiss_post_login_dialogs")
    @patch("luanny.auth._is_logged_in", return_value=True)
    @patch("luanny.auth._detect_block", return_value=False)
    @patch("luanny.auth._detect_checkpoint", return_value=False)
    @patch("luanny.auth._dismiss_cookie_banner")
    @patch("luanny.auth.human_delay_sync")
    @patch("luanny.auth.time")
    def test_login_sucesso(
        self, mock_time, mock_delay, mock_cookies, mock_checkpoint,
        mock_block, mock_logged_in, mock_dismiss, mock_save,
        mock_session, mock_config,
    ):
        """Deve completar login com sucesso e salvar sessão."""
        # Configurar mocks da página
        mock_session.page.wait_for_selector.return_value = MagicMock()
        mock_session.page.locator.return_value = MagicMock()

        result = _perform_login(mock_session, mock_config)

        assert result is True
        mock_save.assert_called_once_with(mock_session.context)

    @patch("luanny.auth._is_logged_in", return_value=False)
    @patch("luanny.auth._detect_block", return_value=True)
    @patch("luanny.auth._detect_checkpoint", return_value=False)
    @patch("luanny.auth._dismiss_cookie_banner")
    @patch("luanny.auth.human_delay_sync")
    @patch("luanny.auth.time")
    def test_login_bloqueado(
        self, mock_time, mock_delay, mock_cookies,
        mock_checkpoint, mock_block, mock_logged_in,
        mock_session, mock_config,
    ):
        """Deve retornar False quando Instagram bloqueia."""
        mock_session.page.wait_for_selector.return_value = MagicMock()
        mock_session.page.locator.return_value = MagicMock()

        result = _perform_login(mock_session, mock_config)

        assert result is False


class TestEnsureAuthenticated:
    """Testes do fluxo principal de autenticação."""

    @patch("luanny.auth._load_session", return_value=True)
    def test_reusa_sessao_existente(self, mock_load, mock_session, mock_config):
        """Deve reusar sessão quando válida, sem fazer login."""
        result = ensure_authenticated(mock_session, mock_config)

        assert result is True
        mock_load.assert_called_once_with(mock_session)

    @patch("luanny.auth._perform_login", return_value=True)
    @patch("luanny.auth._load_session", return_value=False)
    def test_faz_login_quando_sessao_invalida(self, mock_load, mock_login, mock_session, mock_config):
        """Deve fazer login quando sessão não é válida."""
        result = ensure_authenticated(mock_session, mock_config)

        assert result is True
        mock_login.assert_called_once()

    @patch("luanny.auth._perform_login", return_value=False)
    @patch("luanny.auth._load_session", return_value=False)
    def test_falha_irrecuperavel_levanta_system_exit(self, mock_load, mock_login, mock_session, mock_config):
        """Deve levantar SystemExit quando login falha."""
        with pytest.raises(SystemExit):
            ensure_authenticated(mock_session, mock_config)


class TestDetectCheckpoint:
    """Testes de detecção de checkpoint/2FA."""

    def test_detecta_por_seletor(self, mock_session):
        """Deve detectar checkpoint por seletores conhecidos."""
        mock_session.page.url = INSTAGRAM_HOME_URL
        element = MagicMock()
        # Retornar element apenas para o primeiro seletor de checkpoint
        mock_session.page.query_selector.side_effect = [element]

        assert _detect_checkpoint(mock_session.page) is True

    def test_detecta_por_url_challenge(self, mock_session):
        """Deve detectar checkpoint pela URL contendo 'challenge'."""
        mock_session.page.url = "https://www.instagram.com/challenge/"
        mock_session.page.query_selector.return_value = None

        assert _detect_checkpoint(mock_session.page) is True

    def test_detecta_por_url_two_factor(self, mock_session):
        """Deve detectar 2FA pela URL contendo 'two_factor'."""
        mock_session.page.url = "https://www.instagram.com/accounts/two_factor/"
        mock_session.page.query_selector.return_value = None

        assert _detect_checkpoint(mock_session.page) is True

    def test_nao_detecta_em_pagina_normal(self, mock_session):
        """Não deve detectar checkpoint em página normal."""
        mock_session.page.url = INSTAGRAM_HOME_URL
        mock_session.page.query_selector.return_value = None

        assert _detect_checkpoint(mock_session.page) is False


class TestDetectBlock:
    """Testes de detecção de bloqueio."""

    def test_detecta_bloqueio(self, mock_session):
        """Deve detectar bloqueio por indicadores conhecidos."""
        element = MagicMock()
        mock_session.page.query_selector.side_effect = [element]

        assert _detect_block(mock_session.page) is True

    def test_nao_detecta_em_pagina_normal(self, mock_session):
        """Não deve detectar bloqueio em página normal."""
        mock_session.page.query_selector.return_value = None

        assert _detect_block(mock_session.page) is False


class TestIsLoggedIn:
    """Testes de verificação de login."""

    def test_detecta_login_por_indicador(self, mock_session):
        """Deve reconhecer login quando indicador está presente."""
        mock_session.page.url = INSTAGRAM_HOME_URL
        element = MagicMock()
        mock_session.page.query_selector.return_value = element

        assert _is_logged_in(mock_session.page) is True

    def test_nao_detecta_na_pagina_de_login(self, mock_session):
        """Não deve reconhecer login se está na página de login."""
        mock_session.page.url = INSTAGRAM_LOGIN_URL
        mock_session.page.query_selector.return_value = None

        assert _is_logged_in(mock_session.page) is False


class TestInvalidateSession:
    """Testes de invalidação de sessão."""

    @patch("luanny.auth._get_storage_state_path")
    def test_remove_arquivo_existente(self, mock_path):
        """Deve remover o arquivo de storage_state."""
        path = MagicMock()
        path.exists.return_value = True
        mock_path.return_value = path

        _invalidate_session()

        path.unlink.assert_called_once()

    @patch("luanny.auth._get_storage_state_path")
    def test_tolera_arquivo_inexistente(self, mock_path):
        """Não deve falhar se arquivo não existe."""
        path = MagicMock()
        path.exists.return_value = False
        mock_path.return_value = path

        _invalidate_session()  # Não deve levantar exceção

        path.unlink.assert_not_called()
