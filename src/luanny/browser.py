"""
Módulo de inicialização do browser (Playwright).

Responsável por criar e gerenciar o contexto do browser com
configurações apropriadas (idioma pt-BR, viewport, user agent).

STUB — Fase 0: retorna dados mock. Implementação real na Fase 1.
"""

from __future__ import annotations

from typing import Any

from luanny.log import get_logger
from luanny.models import AppConfig

logger = get_logger("browser")


def create_browser_context(config: AppConfig) -> Any:
    """
    Cria e retorna um contexto de browser Playwright configurado.

    Na Fase 0, retorna um placeholder.

    Args:
        config: Configuração da aplicação.

    Returns:
        Contexto do browser (Playwright BrowserContext na implementação real).
    """
    logger.info(
        "browser_stub",
        msg="Browser context criado (stub)",
        headless=config.headless,
        language=config.browser_language,
    )
    return {"_stub": True, "headless": config.headless}


def close_browser_context(context: Any) -> None:
    """
    Fecha o contexto do browser e libera recursos.

    Args:
        context: Contexto do browser a ser fechado.
    """
    logger.info("browser_stub", msg="Browser context fechado (stub)")


async def human_delay(min_seconds: float = 3.0, max_seconds: float = 7.0) -> None:
    """
    Aguarda um tempo aleatório simulando comportamento humano.

    Args:
        min_seconds: Delay mínimo em segundos.
        max_seconds: Delay máximo em segundos.
    """
    import asyncio
    import random

    delay = random.uniform(min_seconds, max_seconds)
    logger.debug("human_delay", seconds=round(delay, 2))
    await asyncio.sleep(delay)
