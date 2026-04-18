"""
Utilitários de paths de runtime para o Luanny.

Centraliza a resolução de diretórios usados pelo aplicativo para que
o comportamento fique previsível tanto em execução via Python quanto
no executável empacotado.
"""

from __future__ import annotations

import sys
from pathlib import Path


def get_runtime_base_dir() -> Path:
    """Retorna a base de runtime do processo atual.

    Em modo frozen, usa o diretório do executável. Em modo normal,
    usa a raiz do repositório.
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parents[2]


def resolve_runtime_path(path_value: str | Path, *, base_dir: Path | None = None) -> Path:
    """Resolve um path relativo a partir da base de runtime."""
    path = Path(path_value)
    if path.is_absolute():
        return path
    return (base_dir or get_runtime_base_dir()) / path


def get_storage_state_path() -> Path:
    """Retorna o caminho do storage_state.json no runtime atual."""
    return get_runtime_base_dir() / "storage_state.json"


def get_logs_dir() -> Path:
    """Retorna o diretório de logs no runtime atual."""
    return get_runtime_base_dir() / "logs"


def find_env_file() -> Path | None:
    """Procura um .env no runtime atual e nos pais relevantes."""
    seen: set[Path] = set()
    search_roots = [Path.cwd(), get_runtime_base_dir()]

    for root in search_roots:
        for directory in [root, *root.parents]:
            if directory in seen:
                continue
            seen.add(directory)
            env_path = directory / ".env"
            if env_path.is_file():
                return env_path
    return None