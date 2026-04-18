"""Tests for CLI wiring and help rendering."""

from __future__ import annotations

import pytest
import typer
from typer.testing import CliRunner

from luanny.cli import app, _validate_max_posts_value


runner = CliRunner()


def test_main_help_renders() -> None:
    """Top-level help should render without crashing."""
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Luanny" in result.output


def test_scrape_help_renders() -> None:
    """Scrape command help should render without crashing."""
    result = runner.invoke(app, ["scrape", "--help"])

    assert result.exit_code == 0
    assert "--since" in result.output
    assert "--until" in result.output


def test_validate_max_posts_value_accepts_supported_range() -> None:
    """Max posts should accept values inside the supported limits."""
    assert _validate_max_posts_value(1) == 1
    assert _validate_max_posts_value(500) == 500


def test_validate_max_posts_value_rejects_out_of_range_values() -> None:
    """Max posts should reject invalid values with user-friendly message."""
    with pytest.raises(typer.BadParameter):
        _validate_max_posts_value(0)

    with pytest.raises(typer.BadParameter):
        _validate_max_posts_value(501)
