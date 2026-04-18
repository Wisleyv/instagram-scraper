"""Tests for persistent incremental collection state (phase 1)."""

from __future__ import annotations

from datetime import datetime, timezone

from luanny.collection_state import (
    get_collection_state_path,
    load_collection_state,
    save_collection_state,
    update_collection_state,
)
from luanny.models import CollectionState, PostRecord


def test_load_collection_state_missing_file(tmp_path):
    """Missing state file should return defaults for the profile."""
    state = load_collection_state("govbr", output_dir=tmp_path)

    assert state.profile == "govbr"
    assert state.collection_id is None
    assert state.seen_post_ids == []
    assert state.last_published_at is None
    assert state.last_post_id is None


def test_save_and_load_collection_state_roundtrip(tmp_path):
    """Saved state must be readable in a later execution."""
    original = CollectionState(
        profile="govbr",
        collection_id="run-001",
        seen_post_ids=["POST_1", "POST_2"],
    )

    state_path = save_collection_state(original, output_dir=tmp_path)

    assert state_path.exists()
    loaded = load_collection_state("govbr", output_dir=tmp_path)

    assert loaded.profile == "govbr"
    assert loaded.collection_id == "run-001"
    assert loaded.seen_post_ids == ["POST_1", "POST_2"]


def test_update_collection_state_merges_ids_and_tracks_oldest_publication():
    """State update should deduplicate ids and store oldest publication."""
    base_state = CollectionState(
        profile="govbr",
        collection_id="run-001",
        seen_post_ids=["POST_A", "POST_B"],
    )

    posts = [
        PostRecord(
            post_id="POST_B",
            post_url="https://www.instagram.com/p/POST_B/",
            profile_username="govbr",
            published_at=datetime(2026, 4, 12, 12, 0, tzinfo=timezone.utc),
        ),
        PostRecord(
            post_id="POST_C",
            post_url="https://www.instagram.com/p/POST_C/",
            profile_username="govbr",
            published_at=datetime(2026, 4, 8, 12, 0, tzinfo=timezone.utc),
        ),
        PostRecord(
            post_id="POST_D",
            post_url="https://www.instagram.com/p/POST_D/",
            profile_username="govbr",
        ),
    ]

    updated = update_collection_state(
        state=base_state,
        posts=posts,
        collection_id="run-002",
    )

    assert updated.collection_id == "run-002"
    assert updated.seen_post_ids == ["POST_A", "POST_B", "POST_C", "POST_D"]
    assert updated.last_post_id == "POST_C"
    assert updated.last_published_at == datetime(
        2026,
        4,
        8,
        12,
        0,
        tzinfo=timezone.utc,
    )


def test_load_collection_state_invalid_json_returns_defaults(tmp_path):
    """Invalid state content should not crash and should reset to defaults."""
    state_path = get_collection_state_path("govbr", output_dir=tmp_path)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text("{invalid-json", encoding="utf-8")

    loaded = load_collection_state("govbr", output_dir=tmp_path)

    assert loaded.profile == "govbr"
    assert loaded.seen_post_ids == []
