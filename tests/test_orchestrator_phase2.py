"""Tests for phase-2 temporal controls in orchestrator."""

from __future__ import annotations

from datetime import date, datetime, timezone

from luanny.models import PostRecord
from luanny.orchestrator import _filter_posts_by_publication_window


def _post(post_id: str, published_at: datetime | None) -> PostRecord:
    return PostRecord(
        post_id=post_id,
        post_url=f"https://www.instagram.com/p/{post_id}/",
        profile_username="govbr",
        published_at=published_at,
    )


def test_filter_posts_by_publication_window_filters_outside_interval() -> None:
    """Posts outside since/until should be removed."""
    posts = [
        _post("P1", datetime(2026, 4, 5, 12, 0, tzinfo=timezone.utc)),
        _post("P2", datetime(2026, 4, 10, 12, 0, tzinfo=timezone.utc)),
        _post("P3", datetime(2026, 4, 20, 12, 0, tzinfo=timezone.utc)),
        _post("P4", datetime(2026, 4, 30, 12, 0, tzinfo=timezone.utc)),
    ]

    filtered, dropped, missing = _filter_posts_by_publication_window(
        posts,
        since=date(2026, 4, 10),
        until=date(2026, 4, 20),
    )

    assert [post.post_id for post in filtered] == ["P2", "P3"]
    assert dropped == 2
    assert missing == 0


def test_filter_posts_by_publication_window_keeps_unknown_dates() -> None:
    """Posts without publication date should remain in phase 2."""
    posts = [
        _post("P1", datetime(2026, 4, 10, 12, 0, tzinfo=timezone.utc)),
        _post("P2", None),
    ]

    filtered, dropped, missing = _filter_posts_by_publication_window(
        posts,
        since=date(2026, 4, 1),
        until=date(2026, 4, 30),
    )

    assert [post.post_id for post in filtered] == ["P1", "P2"]
    assert dropped == 0
    assert missing == 1


def test_filter_posts_by_publication_window_no_window_is_noop() -> None:
    """Without since/until configured, filtering should not change posts."""
    posts = [
        _post("P1", datetime(2026, 4, 10, 12, 0, tzinfo=timezone.utc)),
        _post("P2", None),
    ]

    filtered, dropped, missing = _filter_posts_by_publication_window(
        posts,
        since=None,
        until=None,
    )

    assert [post.post_id for post in filtered] == ["P1", "P2"]
    assert dropped == 0
    assert missing == 0
