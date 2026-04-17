"""
Módulo de exportação de resultados.

Gera saídas em JSON, CSV e relatório de execução.

STUB — Fase 0: simula exportação. Implementação real na Fase 4.
"""

from __future__ import annotations

from luanny.log import get_logger
from luanny.models import AppConfig, CollectionResult

logger = get_logger("exporters")


def export_results(result: CollectionResult, config: AppConfig) -> None:
    """
    Exporta os resultados da coleta em JSON, CSV e relatório.

    Cria a estrutura de diretórios de saída e gera:
      - posts.json (dados completos)
      - summary.csv (resumo tabular)
      - report.md (relatório de execução)

    Args:
        result: Resultado consolidado da coleta.
        config: Configuração da aplicação.
    """
    logger.info(
        "export_stub",
        msg="Exportação simulada (stub)",
        total_posts=len(result.posts),
        output_dir=config.output_dir,
    )


def _export_json(result: CollectionResult, output_path: str) -> str:
    """Exporta dados completos em JSON. Retorna caminho do arquivo."""
    logger.debug("export_stub", msg="JSON export simulado (stub)")
    return f"{output_path}/posts.json"


def _export_csv(result: CollectionResult, output_path: str) -> str:
    """Exporta resumo tabular em CSV (UTF-8 BOM). Retorna caminho do arquivo."""
    logger.debug("export_stub", msg="CSV export simulado (stub)")
    return f"{output_path}/summary.csv"


def _export_report(result: CollectionResult, output_path: str) -> str:
    """Gera relatório de execução em Markdown. Retorna caminho do arquivo."""
    logger.debug("export_stub", msg="Relatório export simulado (stub)")
    return f"{output_path}/report.md"
