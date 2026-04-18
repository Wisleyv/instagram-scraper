"""
Módulo de configuração do Luanny.

Carrega e valida configuração a partir de variáveis de ambiente (.env)
e/ou argumentos passados programaticamente (ex: pela CLI).
Falha cedo e de forma clara quando credenciais ou parâmetros obrigatórios
estão ausentes.
"""

from __future__ import annotations

import os
import sys
from datetime import date
from typing import Callable

from dotenv import load_dotenv

from luanny.models import AppConfig
from luanny.runtime_paths import find_env_file


def _parse_bool(raw: str) -> bool:
    """Converte string para booleano no formato esperado pelo .env."""
    return raw.strip().lower() in ("true", "1", "yes")


def _parse_iso_date(raw: str) -> date:
    """Converte data ISO (AAAA-MM-DD) para date."""
    return date.fromisoformat(raw.strip())


def _apply_override_value(
    override_value: object,
    converter: Callable[[str], object],
) -> object:
    """Aplica parsing apenas quando o override vem como string."""
    if not isinstance(override_value, str):
        return override_value
    if converter is str:
        return override_value
    return converter(override_value)


def load_config(**overrides: object) -> AppConfig:
    """
    Carrega configuração do ambiente e retorna AppConfig validado.

    Args:
        **overrides: Valores que sobrescrevem os do .env (usados pela CLI).

    Returns:
        AppConfig validado.

    Raises:
        SystemExit: Se credenciais obrigatórias estão ausentes.
    """
    # Carregar .env se existir
    env_file = find_env_file()
    if env_file:
        load_dotenv(env_file, override=False)

    # Montar dict de configuração a partir do ambiente
    env_values: dict[str, object] = {}

    # Credenciais (obrigatórias)
    username = (
        overrides.get("instagram_username") or os.getenv("INSTAGRAM_USERNAME")
    )
    password = (
        overrides.get("instagram_password") or os.getenv("INSTAGRAM_PASSWORD")
    )

    if not username or not password:
        print(
            "\n╔══════════════════════════════════════════════════════════"
            "════╗"
            "\n║  ERRO: Credenciais do Instagram não configuradas.          ║"
            "\n║                                                            ║"
            "\n║  Crie um arquivo .env baseado em .env.example e preencha:  ║"
            "\n║    INSTAGRAM_USERNAME=sua_conta                            ║"
            "\n║    INSTAGRAM_PASSWORD=sua_senha                            ║"
            "\n╚══════════════════════════════════════════════════════════"
            "════╝"
            "\n",
            file=sys.stderr,
        )
        raise SystemExit(1)

    env_values["instagram_username"] = username
    env_values["instagram_password"] = password

    # Parâmetros opcionais do ambiente
    _optional_mappings: dict[str, tuple[str, Callable[[str], object]]] = {
        "MAX_POSTS": ("max_posts", int),
        "HEADLESS": ("headless", _parse_bool),
        "CAPTURE_EVIDENCE": (
            "capture_evidence",
            _parse_bool,
        ),
        "BROWSER_LANGUAGE": ("browser_language", str),
        "NAVIGATION_TIMEOUT": ("navigation_timeout", int),
        "ELEMENT_TIMEOUT": ("element_timeout", int),
        "DELAY_MIN": ("delay_min", float),
        "DELAY_MAX": ("delay_max", float),
        "OUTPUT_DIR": ("output_dir", str),
        "SINCE": ("since", _parse_iso_date),
        "UNTIL": ("until", _parse_iso_date),
        "RESUME": ("resume", _parse_bool),
    }

    for env_key, (field_name, converter) in _optional_mappings.items():
        # Override explícito tem prioridade sobre .env
        if field_name in overrides and overrides[field_name] is not None:
            try:
                env_values[field_name] = _apply_override_value(
                    overrides[field_name],
                    converter,
                )
            except (ValueError, TypeError):
                print(
                    (
                        f"AVISO: Override inválido para {field_name}="
                        f"{overrides[field_name]!r}, usando padrão."
                    ),
                    file=sys.stderr,
                )
        else:
            raw = os.getenv(env_key)
            if raw is not None:
                try:
                    env_values[field_name] = converter(raw)
                except (ValueError, TypeError):
                    print(
                        (
                            f"AVISO: Valor inválido para {env_key}={raw!r}, "
                            "usando padrão."
                        ),
                        file=sys.stderr,
                    )

    return AppConfig(**env_values)
