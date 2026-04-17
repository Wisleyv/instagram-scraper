"""
Módulo de autenticação do Instagram.

Gerencia login, persistência de sessão (storage_state) e
detecção de checkpoints/2FA.

STUB — Fase 0: simula autenticação. Implementação real na Fase 1.
"""

from __future__ import annotations

from typing import Any

from luanny.log import get_logger
from luanny.models import AppConfig

logger = get_logger("auth")


def ensure_authenticated(browser_context: Any, config: AppConfig) -> bool:
    """
    Garante que o browser está autenticado no Instagram.

    Tenta reusar sessão salva; se inválida, faz novo login.

    Args:
        browser_context: Contexto do browser Playwright.
        config: Configuração da aplicação.

    Returns:
        True se autenticação bem-sucedida.

    Raises:
        SystemExit: Se autenticação falhar irrecuperavelmente.
    """
    logger.info(
        "auth_stub",
        msg="Autenticação simulada (stub)",
        username=config.instagram_username,
    )
    return True


def _load_session(browser_context: Any) -> bool:
    """Tenta carregar sessão salva. Retorna True se válida."""
    logger.debug("auth_stub", msg="Carregamento de sessão simulado (stub)")
    return False


def _perform_login(browser_context: Any, config: AppConfig) -> bool:
    """Realiza login com credenciais. Retorna True se bem-sucedido."""
    logger.debug("auth_stub", msg="Login simulado (stub)")
    return True


def _handle_checkpoint(browser_context: Any) -> None:
    """Detecta e trata checkpoint/2FA no modo headed."""
    logger.debug("auth_stub", msg="Verificação de checkpoint simulada (stub)")
