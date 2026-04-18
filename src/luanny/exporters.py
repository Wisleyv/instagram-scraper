"""
Módulo de exportação de resultados.

Gera saídas em JSON, CSV e relatório de execução.
"""

from __future__ import annotations

import json
from pathlib import Path

import csv
from luanny.log import get_logger
from luanny.models import AppConfig, CollectionResult, AltTextSource
from luanny.runtime_paths import resolve_runtime_path

logger = get_logger("exporters")


def export_results(
    result: CollectionResult,
    config: AppConfig,
    base_output_dir: Path | None = None,
) -> None:
    """
    Exporta os resultados da coleta em JSON, CSV e relatório.

    Cria a estrutura de diretórios de saída e gera:
      - posts.json (dados completos)
      - summary.csv (resumo tabular)
      - report.md (relatório de execução)

    Args:
        result: Resultado consolidado da coleta.
        config: Configuração da aplicação.
        base_output_dir: Diretório raiz da run atual.
    """
    export_dir = (
        base_output_dir
        if base_output_dir
        else resolve_runtime_path(config.output_dir)
    )
    export_dir.mkdir(parents=True, exist_ok=True)

    logger.info(
        "exporting_data",
        total_posts=len(result.posts),
        export_dir=str(export_dir),
    )

    _export_json(result, export_dir)

    if result.posts:
        _export_csv(result, export_dir)

    _export_report(result, export_dir)

    logger.info("export_finished", export_dir=str(export_dir))


def _export_json(result: CollectionResult, export_dir: Path) -> Path:
    """Exporta dados completos em JSON. Retorna caminho do arquivo."""
    out_path = export_dir / "posts.json"

    # mode='json' serializa datetimes corretamente
    data = result.model_dump(mode="json", exclude_none=True)

    out_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.debug("exported_json", path=str(out_path))
    return out_path


def _export_csv(result: CollectionResult, export_dir: Path) -> Path:
    """Exporta resumo tabular em CSV (UTF-8 BOM). Retorna o caminho."""
    out_path = export_dir / "summary.csv"

    if not result.posts:
        # Se não há posts, cria um vazio para manter a estrutura
        out_path.write_text("post_id\n", encoding="utf-8-sig")
        return out_path

    rows = []
    keys = [
        "post_id",
        "post_url",
        "published_at",
        "post_type",
        "is_video",
        "is_carousel",
        "media_count",
        "hashtags",
        "mentions",
        "caption_preview",
        "alts_joined",
        "has_auto_alt_tag",
        "has_manual_alt_tag",
    ]

    for p in result.posts:
        media_count = len(p.media)
        # Extrair todos os alts encontrados
        alts = [m.alt_text for m in p.media if m.alt_text]
        caption_preview = (
            (p.caption or "").replace("\n", " ").replace("\r", " ")[:150]
        )
        has_manual_alt_tag = any(
            m.alt_text_source == AltTextSource.MANUAL for m in p.media
        )

        row = {
            "post_id": p.post_id,
            "post_url": p.post_url,
            "published_at": (
                p.published_at.isoformat() if p.published_at else ""
            ),
            "post_type": p.post_type.value,
            "is_video": p.is_video,
            "is_carousel": p.is_carousel,
            "media_count": media_count,
            "hashtags": " ".join(p.hashtags),
            "mentions": " ".join(p.mentions),
            "caption_preview": caption_preview,
            "alts_joined": " | ".join(alts) if alts else "",
            "has_auto_alt_tag": any(m.is_auto_generated_alt for m in p.media),
            "has_manual_alt_tag": has_manual_alt_tag,
        }
        rows.append(row)

    with open(
        out_path,
        mode="w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)

    logger.debug("exported_csv", path=str(out_path))
    return out_path


def _export_report(result: CollectionResult, export_dir: Path) -> Path:
    """Gera relatório de execução em Markdown. Retorna caminho do arquivo."""
    out_path = export_dir / "report.md"

    meta = result.metadata

    success_posts = len(result.posts)
    errors_count = sum(len(p.errors) for p in result.posts)

    duration_str = "N/A"
    if meta.started_at and meta.finished_at:
        duration_seconds = (meta.finished_at - meta.started_at).total_seconds()
        duration_str = f"{duration_seconds:.2f}"

    videos_found = sum(1 for p in result.posts if p.is_video)
    carousels_found = sum(1 for p in result.posts if p.is_carousel)
    images_found = sum(
        1 for p in result.posts if not p.is_carousel and not p.is_video
    )

    requested_posts = meta.max_posts_requested
    auto_alt_count = sum(
        any(m.is_auto_generated_alt for m in p.media) for p in result.posts
    )
    manual_alt_count = sum(
        any(m.alt_text_source == AltTextSource.MANUAL for m in p.media)
        for p in result.posts
    )
    footer_note = (
        f"*Gerado por Luanny Scraper v{meta.collector_version}. "
        "Valide os JSON e CSV em anexo.*"
    )

    md_content = f"""# Relatório de Coleta - Luanny Acessibilidade

## Metadados da Execução
- **Perfil Solicitado:** {meta.target_profile}
- **Início:** {meta.started_at}
- **Fim:** {meta.finished_at}
- **Duração Total (s):** {duration_str}
- **Versão:** {meta.collector_version}

## Métricas
- **Posts Coletados (Sucesso Total/Parcial):** {success_posts} /
    {requested_posts} solicitados
- **Vídeos encontrados:** {videos_found}
- **Carrosséis encontrados:** {carousels_found}
- **Imagens individuais:** {images_found}
- **Erros registrados:** {errors_count}

## Visão Geral da Acessibilidade
*(Gerado automaticamente sobre a amostra processada habilitada)*

- Auto-Generated Alts identificados pelo Robô: {auto_alt_count}
- Manual Alts identificados pelo Robô: {manual_alt_count}

---
{footer_note}
"""
    out_path.write_text(md_content, encoding="utf-8")
    logger.debug("exported_report", path=str(out_path))
    return out_path
