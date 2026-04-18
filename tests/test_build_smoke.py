"""Tests for phase-5 Windows distribution smoke checks."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from luanny.build_smoke import (
    SmokeCheckError,
    run_windows_distribution_smoke_checks,
)


def _prepare_dist_artifacts(tmp_path: Path) -> Path:
    dist_dir = tmp_path / "dist" / "Luanny"
    dist_dir.mkdir(parents=True, exist_ok=True)
    (dist_dir / "Luanny.exe").write_text(
        "binary-placeholder",
        encoding="utf-8",
    )
    (dist_dir / "executar.bat").write_text("@echo off\n", encoding="utf-8")
    return dist_dir


def test_smoke_checks_require_dist_artifacts(tmp_path: Path) -> None:
    """Smoke checks should fail fast if dist artifacts are missing."""
    dist_dir = tmp_path / "dist" / "Luanny"
    dist_dir.mkdir(parents=True, exist_ok=True)

    with pytest.raises(SmokeCheckError) as exc_info:
        run_windows_distribution_smoke_checks(dist_dir)

    assert "Luanny.exe" in str(exc_info.value)
    assert "executar.bat" in str(exc_info.value)


def test_smoke_checks_run_help_and_launcher(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Smoke checks should run executable help and launcher scripted flow."""
    dist_dir = _prepare_dist_artifacts(tmp_path)
    calls: list[tuple[list[str], dict[str, object]]] = []

    def fake_run(
        command: list[str],
        **kwargs: object,
    ) -> subprocess.CompletedProcess[str]:
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 0, stdout="ok", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)

    run_windows_distribution_smoke_checks(dist_dir, timeout_seconds=15)

    assert len(calls) == 2

    first_command, first_kwargs = calls[0]
    assert first_command == [str(dist_dir / "Luanny.exe"), "--help"]
    assert first_kwargs["cwd"] == dist_dir
    assert first_kwargs["timeout"] == 15

    second_command, second_kwargs = calls[1]
    assert second_command[0:2] == ["cmd", "/c"]
    assert second_command[2] == str(dist_dir / "executar.bat")
    assert second_kwargs["cwd"] == dist_dir
    assert second_kwargs["input"] == "2\n\n3\n"


def test_smoke_checks_optionally_run_regression_tests(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Smoke checks may include optional full regression execution."""
    dist_dir = _prepare_dist_artifacts(tmp_path)
    calls: list[tuple[list[str], dict[str, object]]] = []

    def fake_run(
        command: list[str],
        **kwargs: object,
    ) -> subprocess.CompletedProcess[str]:
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 0, stdout="ok", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)

    run_windows_distribution_smoke_checks(
        dist_dir,
        run_regression_tests=True,
        regression_timeout_seconds=90,
        repo_root=tmp_path,
        python_executable="python-custom",
    )

    assert len(calls) == 3

    command, kwargs = calls[2]
    assert command == ["python-custom", "-m", "pytest", "-q"]
    assert kwargs["cwd"] == tmp_path
    assert kwargs["timeout"] == 90


def test_smoke_checks_raise_readable_error_on_failed_command(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Command failures should be converted into actionable messages."""
    dist_dir = _prepare_dist_artifacts(tmp_path)

    def fake_run(
        command: list[str],
        **kwargs: object,
    ) -> subprocess.CompletedProcess[str]:
        if command and command[0].endswith("Luanny.exe"):
            raise subprocess.CalledProcessError(
                returncode=2,
                cmd=command,
                output="mock-stdout",
                stderr="mock-stderr",
            )
        return subprocess.CompletedProcess(command, 0, stdout="ok", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)

    with pytest.raises(SmokeCheckError) as exc_info:
        run_windows_distribution_smoke_checks(dist_dir)

    msg = str(exc_info.value)
    assert "Luanny.exe --help" in msg
    assert "mock-stdout" in msg
    assert "mock-stderr" in msg
