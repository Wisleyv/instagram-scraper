"""
Testes de robustez e resiliência (Fase 5).

Verifica retries, limitação de taxa e detecção de bloqueios.
"""

from __future__ import annotations

import time
from unittest.mock import MagicMock, call

import pytest
from playwright.sync_api import Error as PlaywrightError

from luanny.auth import _load_session, BLOCK_INDICATORS
from luanny.browser import human_delay_sync
from luanny.models import AppConfig
from luanny.post_extractor import extract_post


def test_human_delay_sync(monkeypatch):
    """Testa se o delay funciona dentro dos limites."""
    # Mock do sleep para não atrasar o teste real
    mock_sleep = MagicMock()
    monkeypatch.setattr(time, "sleep", mock_sleep)
    
    human_delay_sync(1.0, 2.0)
    mock_sleep.assert_called_once()
    args, _ = mock_sleep.call_args
    assert 1.0 <= args[0] <= 2.0


def test_extractor_retry_on_network_error(monkeypatch):
    """Testa se o post_extractor tenta novamente (retry via tenacity) em erro de rede TCP/Playwright."""
    mock_session = MagicMock()
    mock_config = AppConfig(
        instagram_username="test",
        instagram_password="pwd",
        navigation_timeout=5000, 
    )
    
    # Configuramos o page.goto para falhar nas primeiras execuções e passar na terceira
    call_count = 0
    def mock_goto(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise PlaywrightError("net::ERR_CONNECTION_RESET")
        return None
        
    mock_session.page.goto.side_effect = mock_goto
    mock_session.page.query_selector.return_value = None # Mock DOM
    
    # Substituir sleep do extractor pra rodar rápido
    monkeypatch.setattr(time, "sleep", lambda x: None)
    
    record = extract_post(
        session=mock_session,
        post_id="P_RETRY_123",
        post_url="https://inst.com/p",
        profile_username="test",
        config=mock_config
    )
    
    assert record.post_id == "P_RETRY_123"
    assert call_count == 3  # Provando que o retry tentou 3 vezes antes de prosseguir


def test_auth_block_detection(monkeypatch):
    """Testa se _load_session aborta ao detectar tela de bloqueio da Meta (Action block)."""
    mock_session = MagicMock()
    monkeypatch.setattr(time, "sleep", lambda x: None)
    
    # Falsifica o storage path existir
    path_mock = MagicMock()
    path_mock.exists.return_value = True
    monkeypatch.setattr("luanny.auth._get_storage_state_path", lambda: path_mock)
    
    # Mock para query selector retornar True apenas no seletor de bloqueio
    def mock_query_selector(selector):
        if selector in BLOCK_INDICATORS:
            return MagicMock() # Achou um bloqueio ("Aguarde" ou "Suspicious activity")
        return None
        
    mock_session.page.query_selector.side_effect = mock_query_selector
    
    # load_session deve retornar False (e logar erro internamente) em vez de validar a sessão
    is_valid = _load_session(mock_session)
    
    assert is_valid is False
