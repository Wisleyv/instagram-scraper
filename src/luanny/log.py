"""
Módulo de logging estruturado do Luanny.

Configura structlog para produzir logs legíveis no terminal e,
opcionalmente, em arquivo. Cada entrada de log carrega contexto
relevante (execução, perfil, post).
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import structlog

from luanny.runtime_paths import get_logs_dir


_configured = False


def setup_logging(
    *,
    log_dir: str | Path | None = None,
    verbose: bool = False,
) -> None:
    """
    Configura o logging estruturado para a aplicação.

    Args:
        log_dir: Diretório para salvar arquivos de log.
        verbose: Se True, exibe logs DEBUG no terminal.
    """
    global _configured
    if _configured:
        return

    log_path = Path(log_dir) if log_dir is not None else get_logs_dir()
    log_path.mkdir(parents=True, exist_ok=True)

    # Nível base
    log_level = logging.DEBUG if verbose else logging.INFO

    # Configurar logging padrão do Python (para bibliotecas que usam logging)
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stderr,
        level=log_level,
    )

    # Configurar structlog
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer(colors=sys.stderr.isatty()),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(file=sys.stderr),
        cache_logger_on_first_use=True,
    )

    _configured = True


def get_logger(
    name: str | None = None,
    **initial_context: object,
) -> structlog.stdlib.BoundLogger:
    """
    Retorna um logger estruturado com contexto inicial.

    Args:
        name: Nome do módulo (ex: 'auth', 'extractor').
        **initial_context: Campos adicionais de contexto.

    Returns:
        Logger estruturado com bind de contexto.
    """
    if not _configured:
        setup_logging()

    logger = structlog.get_logger()
    if name:
        logger = logger.bind(module=name)
    if initial_context:
        logger = logger.bind(**initial_context)
    return logger
