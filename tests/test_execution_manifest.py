"""Tests for phase-4 execution manifest generation."""

from __future__ import annotations

import json
from datetime import date, datetime, timezone

from luanny.execution_manifest import (
    create_audit_event,
    write_execution_manifest,
)
from luanny.models import AppConfig, CollectionMetadata, CollectionState


def _base_config(output_dir: str, *, resume: bool) -> AppConfig:
    return AppConfig(
        instagram_username="test_user",
        instagram_password="test_pass",
        output_dir=output_dir,
        resume=resume,
        since=date(2026, 4, 1),
        until=date(2026, 4, 30),
    )


def _base_metadata() -> CollectionMetadata:
    return CollectionMetadata(
        target_profile="govbr",
        profile_url="https://www.instagram.com/govbr/",
        started_at=datetime(2026, 4, 17, 20, 0, tzinfo=timezone.utc),
        finished_at=datetime(2026, 4, 17, 20, 5, tzinfo=timezone.utc),
        collector_version="0.1.0",
        max_posts_requested=10,
        posts_discovered=9,
        posts_collected=8,
        posts_failed=1,
        posts_partial=0,
    )


def test_write_execution_manifest_with_resume_checkpoint(tmp_path):
    """Manifest should include artifacts, hashes, checkpoint and audit."""
    run_dir = tmp_path / "govbr_20260417_200000"
    run_dir.mkdir(parents=True, exist_ok=True)

    (run_dir / "posts.json").write_text('{"ok": true}', encoding="utf-8")
    (run_dir / "summary.csv").write_text("post_id\nP1\n", encoding="utf-8")
    (run_dir / "report.md").write_text("# Report\n", encoding="utf-8")

    state_path = tmp_path / "_state" / "govbr.json"
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text('{"profile": "govbr"}', encoding="utf-8")

    state_before = CollectionState(
        profile="govbr",
        collection_id="run-old",
        seen_post_ids=["P1", "P2"],
        last_post_id="P2",
        last_published_at=datetime(2026, 4, 12, 10, 0, tzinfo=timezone.utc),
    )
    state_after = CollectionState(
        profile="govbr",
        collection_id="run-new",
        seen_post_ids=["P1", "P2", "P3"],
        last_post_id="P3",
        last_published_at=datetime(2026, 4, 10, 10, 0, tzinfo=timezone.utc),
    )

    audit_trail = [
        create_audit_event("state_load", "completed", known_post_ids=2),
        create_audit_event("discovery", "completed", posts_discovered=9),
        create_audit_event("export", "completed"),
    ]

    manifest_path = write_execution_manifest(
        run_dir=run_dir,
        metadata=_base_metadata(),
        config=_base_config(str(tmp_path), resume=True),
        state_before=state_before,
        state_after=state_after,
        state_path=state_path,
        dropped_by_window=1,
        missing_publication_date=2,
        audit_trail=audit_trail,
    )

    data = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert data["manifest_version"] == "1.0"
    assert data["profile"] == "govbr"
    assert data["resume_checkpoint"]["enabled"] is True
    assert data["resume_checkpoint"]["before"]["seen_post_ids_count"] == 2
    assert data["resume_checkpoint"]["after"]["seen_post_ids_count"] == 3
    assert data["counts"]["posts_dropped_by_window"] == 1
    assert data["counts"]["posts_missing_publication_date"] == 2
    assert len(data["audit_trail"]) == 3

    artifacts = data["artifacts"]
    assert "posts.json" in artifacts
    assert "summary.csv" in artifacts
    assert "report.md" in artifacts
    assert "state_file" in artifacts
    assert len(artifacts["posts.json"]["sha256"]) == 64


def test_write_execution_manifest_without_resume_or_csv(tmp_path):
    """Manifest should tolerate optional artifacts and disabled resume."""
    run_dir = tmp_path / "govbr_20260417_210000"
    run_dir.mkdir(parents=True, exist_ok=True)

    (run_dir / "posts.json").write_text('{"ok": true}', encoding="utf-8")
    (run_dir / "report.md").write_text("# Report\n", encoding="utf-8")

    audit_trail = [
        create_audit_event(
            "state_load",
            "skipped",
            reason="resume_disabled",
        ),
    ]

    manifest_path = write_execution_manifest(
        run_dir=run_dir,
        metadata=_base_metadata(),
        config=_base_config(str(tmp_path), resume=False),
        state_before=None,
        state_after=None,
        state_path=None,
        dropped_by_window=0,
        missing_publication_date=0,
        audit_trail=audit_trail,
    )

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    artifacts = data["artifacts"]

    assert data["resume_checkpoint"]["enabled"] is False
    assert data["resume_checkpoint"]["before"] is None
    assert data["resume_checkpoint"]["after"] is None
    assert "summary.csv" not in artifacts
    assert "state_file" not in artifacts
    assert len(data["audit_trail"]) == 1
