"""Execution manifest and audit trail helpers.

Phase 4 adds a per-run manifest that records:
- run metadata and temporal controls;
- checkpoint information for incremental resume state;
- exported artifacts with hashes;
- an explicit audit trail of pipeline steps.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from luanny.log import get_logger
from luanny.models import AppConfig, CollectionMetadata, CollectionState

logger = get_logger("execution_manifest")


def create_audit_event(
    step: str,
    status: str,
    **details: object,
) -> dict[str, Any]:
    """Create a JSON-serializable audit event for one pipeline step."""
    return {
        "step": step,
        "status": status,
        "at": datetime.now(timezone.utc).isoformat(),
        "details": {
            key: _serialize_value(value)
            for key, value in details.items()
        },
    }


def write_execution_manifest(
    *,
    run_dir: Path,
    metadata: CollectionMetadata,
    config: AppConfig,
    state_before: CollectionState | None,
    state_after: CollectionState | None,
    state_path: Path | None,
    dropped_by_window: int,
    missing_publication_date: int,
    audit_trail: list[dict[str, Any]],
) -> Path:
    """Write a phase-4 execution manifest JSON file in run_dir."""
    run_dir.mkdir(parents=True, exist_ok=True)

    payload = {
        "manifest_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "collection_id": metadata.collection_id,
        "profile": metadata.target_profile,
        "profile_url": metadata.profile_url,
        "time_window": {
            "since": _serialize_value(config.since),
            "until": _serialize_value(config.until),
        },
        "resume_checkpoint": {
            "enabled": config.resume,
            "state_path": _path_for_manifest(state_path, run_dir),
            "before": _snapshot_state(state_before),
            "after": _snapshot_state(state_after),
        },
        "counts": {
            "max_posts_requested": metadata.max_posts_requested,
            "posts_discovered": metadata.posts_discovered,
            "posts_collected": metadata.posts_collected,
            "posts_failed": metadata.posts_failed,
            "posts_partial": metadata.posts_partial,
            "posts_dropped_by_window": dropped_by_window,
            "posts_missing_publication_date": missing_publication_date,
        },
        "artifacts": _collect_artifacts(run_dir, state_path),
        "audit_trail": [_serialize_value(event) for event in audit_trail],
    }

    out_path = run_dir / "manifest.json"
    out_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    logger.info(
        "manifest_written",
        path=str(out_path),
        collection_id=metadata.collection_id,
    )
    return out_path


def _collect_artifacts(
    run_dir: Path,
    state_path: Path | None,
) -> dict[str, dict[str, Any]]:
    """Collect hash and size information for exported artifacts."""
    artifacts: dict[str, dict[str, Any]] = {}

    for artifact_name in ("posts.json", "summary.csv", "report.md"):
        artifact_path = run_dir / artifact_name
        if not artifact_path.exists():
            continue
        artifacts[artifact_name] = _describe_file(artifact_path, run_dir)

    if state_path is not None and state_path.exists():
        artifacts["state_file"] = _describe_file(state_path, run_dir)

    return artifacts


def _describe_file(path: Path, run_dir: Path) -> dict[str, Any]:
    """Describe one file for manifest tracking."""
    return {
        "path": _path_for_manifest(path, run_dir),
        "size_bytes": path.stat().st_size,
        "sha256": _compute_sha256(path),
    }


def _compute_sha256(path: Path) -> str:
    """Compute SHA-256 for one file path."""
    digest = hashlib.sha256()
    with path.open("rb") as file_obj:
        for chunk in iter(lambda: file_obj.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _snapshot_state(state: CollectionState | None) -> dict[str, Any] | None:
    """Create a compact checkpoint snapshot from CollectionState."""
    if state is None:
        return None

    return {
        "collection_id": state.collection_id,
        "seen_post_ids_count": len(state.seen_post_ids),
        "last_published_at": _serialize_value(state.last_published_at),
        "last_post_id": state.last_post_id,
        "updated_at": _serialize_value(state.updated_at),
    }


def _path_for_manifest(path: Path | None, run_dir: Path) -> str | None:
    """Return a stable path string for the manifest payload."""
    if path is None:
        return None

    resolved = path.resolve()
    run_resolved = run_dir.resolve()
    try:
        return resolved.relative_to(run_resolved).as_posix()
    except ValueError:
        return resolved.as_posix()


def _serialize_value(value: object) -> Any:
    """Serialize runtime values (date, datetime, Path, containers)."""
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, Path):
        return value.as_posix()
    if isinstance(value, dict):
        return {
            str(key): _serialize_value(item)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple, set)):
        return [_serialize_value(item) for item in value]
    return value
