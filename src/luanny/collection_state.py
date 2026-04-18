"""Utilities for persistent incremental collection state.

Phase 1 introduces a profile-level state file to avoid reprocessing
posts that were already collected in previous runs.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from luanny.log import get_logger
from luanny.models import CollectionState, PostRecord
from luanny.runtime_paths import resolve_runtime_path

logger = get_logger("collection_state")

_STATE_DIRNAME = "_state"


def _normalize_profile(profile: str) -> str:
    """Normalize profile name for state file naming."""
    cleaned = profile.strip().lower().replace("/", "_")
    return cleaned or "unknown_profile"


def get_collection_state_path(
    profile: str,
    output_dir: str | Path = "data",
) -> Path:
    """Return the JSON path used to persist state for one profile."""
    normalized_profile = _normalize_profile(profile)
    base_output = resolve_runtime_path(output_dir)
    return base_output / _STATE_DIRNAME / f"{normalized_profile}.json"


def load_collection_state(
    profile: str,
    output_dir: str | Path = "data",
) -> CollectionState:
    """Load persisted state for a profile, returning defaults if absent."""
    state_path = get_collection_state_path(profile, output_dir)
    if not state_path.exists():
        logger.info(
            "collection_state_not_found",
            profile=profile,
            path=str(state_path),
        )
        return CollectionState(profile=profile)

    try:
        raw_text = state_path.read_text(encoding="utf-8")
        parsed = CollectionState.model_validate_json(raw_text)
    except Exception as exc:
        logger.warning(
            "collection_state_invalid",
            profile=profile,
            path=str(state_path),
            error=str(exc),
        )
        return CollectionState(profile=profile)

    if parsed.profile != profile:
        logger.warning(
            "collection_state_profile_mismatch",
            profile_requested=profile,
            profile_state=parsed.profile,
            path=str(state_path),
        )
        parsed = parsed.model_copy(update={"profile": profile})

    return parsed


def save_collection_state(
    state: CollectionState,
    output_dir: str | Path = "data",
) -> Path:
    """Persist a profile state as JSON and return the written path."""
    state_path = get_collection_state_path(state.profile, output_dir)
    state_path.parent.mkdir(parents=True, exist_ok=True)

    state_to_save = state.model_copy(
        update={"updated_at": datetime.now(timezone.utc)}
    )
    state_path.write_text(
        state_to_save.model_dump_json(indent=2),
        encoding="utf-8",
    )

    logger.info(
        "collection_state_saved",
        profile=state.profile,
        path=str(state_path),
        seen_posts=len(state_to_save.seen_post_ids),
    )
    return state_path


def update_collection_state(
    state: CollectionState,
    posts: Iterable[PostRecord],
    collection_id: str,
) -> CollectionState:
    """Return an updated state with new post ids and oldest publication."""
    post_list = list(posts)
    existing_ids = list(state.seen_post_ids)
    merged_ids = _merge_ids(existing_ids, [post.post_id for post in post_list])

    updates: dict[str, object] = {
        "collection_id": collection_id,
        "seen_post_ids": merged_ids,
        "updated_at": datetime.now(timezone.utc),
    }

    oldest_post = _get_oldest_post_with_publication(post_list)
    if oldest_post is not None:
        should_update_oldest = (
            state.last_published_at is None
            or oldest_post.published_at < state.last_published_at
        )
        if should_update_oldest:
            updates["last_published_at"] = oldest_post.published_at
            updates["last_post_id"] = oldest_post.post_id

    return state.model_copy(update=updates)


def _merge_ids(existing: list[str], new_ids: Iterable[str]) -> list[str]:
    """Merge ids preserving first-seen order and removing duplicates."""
    merged: list[str] = []
    seen: set[str] = set()

    for post_id in [*existing, *list(new_ids)]:
        if not post_id or post_id in seen:
            continue
        seen.add(post_id)
        merged.append(post_id)

    return merged


def _get_oldest_post_with_publication(
    posts: list[PostRecord],
) -> PostRecord | None:
    """Return the post with the oldest published_at, ignoring null dates."""
    dated_posts = [post for post in posts if post.published_at is not None]
    if not dated_posts:
        return None
    return min(dated_posts, key=lambda post: post.published_at)
