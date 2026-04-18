"""
Testes do módulo exporters — Fase 4.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import pytest

from luanny.exporters import export_results
from luanny.models import (
    AltTextSource,
    AppConfig,
    CollectionMetadata,
    CollectionResult,
    MediaItem,
    MediaType,
    PostRecord,
    PostType,
)


@pytest.fixture()
def mock_config() -> AppConfig:
    return AppConfig(
        instagram_username="test",
        instagram_password="pwd",
        output_dir="test_data",
    )


@pytest.fixture()
def sample_result() -> CollectionResult:
    meta = CollectionMetadata(
        target_profile="test_profile",
        profile_url="https://inst.com/test",
        started_at=datetime.now(timezone.utc),
        finished_at=datetime.now(timezone.utc),
        collector_version="0.1.0",
        max_posts_requested=2,
        posts_discovered=2,
        posts_collected=2,
        posts_failed=0,
        posts_partial=0,
    )

    p1 = PostRecord(
        post_id="P1",
        post_url="url1",
        profile_username="test_profile",
        published_at=datetime(2026, 4, 15, 12, 0, tzinfo=timezone.utc),
        caption="Post 1",
        hashtags=["#a"],
        post_type=PostType.IMAGE,
        media=[
            MediaItem(
                media_index=0,
                media_type=MediaType.IMAGE,
                alt_text="Alt 1",
                alt_text_source=AltTextSource.MANUAL,
            )
        ],
    )

    p2 = PostRecord(
        post_id="P2",
        post_url="url2",
        profile_username="test_profile",
        caption="Post 2",
        is_video=True,
        post_type=PostType.VIDEO,
        media=[
            MediaItem(
                media_index=0,
                media_type=MediaType.VIDEO,
            )
        ],
    )

    return CollectionResult(metadata=meta, posts=[p1, p2])


def test_export_results(sample_result, mock_config, tmp_path):
    """Testa se os arquivos JSON, CSV e MD são gerados corretamente."""
    export_results(sample_result, mock_config, base_output_dir=tmp_path)

    # Verifica JSON
    json_path = tmp_path / "posts.json"
    assert json_path.exists()
    data = json.loads(json_path.read_text("utf-8"))
    assert data["metadata"]["target_profile"] == "test_profile"
    assert len(data["posts"]) == 2

    # Verifica CSV
    csv_path = tmp_path / "summary.csv"
    assert csv_path.exists()
    df = pd.read_csv(csv_path)
    assert len(df) == 2
    assert "post_id" in df.columns
    assert "published_at" in df.columns
    assert "alts_joined" in df.columns
    # Verifica o valor extraido da imagem (p1 tem Alt 1)
    assert df.iloc[0]["alts_joined"] == "Alt 1"
    # Verifica que as booleanas the heurísticas estão presentes
    assert "has_auto_alt_tag" in df.columns

    # Verifica Relatório MD
    report_path = tmp_path / "report.md"
    assert report_path.exists()
    report_text = report_path.read_text("utf-8")
    assert "test_profile" in report_text
    assert "**Erros registrados:** 0" in report_text
