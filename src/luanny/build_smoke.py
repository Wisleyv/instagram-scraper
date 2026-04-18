"""Smoke checks for Windows distribution artifacts.

Phase 5 adds automated checks after the PyInstaller build so we can validate
the generated executable package before considering the build successful.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


class SmokeCheckError(RuntimeError):
    """Raised when a smoke check fails."""


def run_windows_distribution_smoke_checks(
    dist_dir: str | Path,
    *,
    timeout_seconds: int = 60,
    run_regression_tests: bool = False,
    regression_timeout_seconds: int = 1200,
    repo_root: str | Path | None = None,
    python_executable: str | Path | None = None,
) -> None:
    """Run smoke checks against a built Windows distribution.

    Args:
        dist_dir: Directory that should contain ``Luanny.exe`` and
            ``executar.bat``.
        timeout_seconds: Timeout used by distribution smoke commands.
        run_regression_tests: If True, run ``pytest -q`` after smoke checks.
        regression_timeout_seconds: Timeout for optional pytest execution.
        repo_root: Repository root used when running pytest.
        python_executable: Python interpreter for optional pytest execution.

    Raises:
        SmokeCheckError: If any check fails.
    """
    dist_path = Path(dist_dir).resolve()
    exe_path = (dist_path / "Luanny.exe").resolve()
    launcher_path = (dist_path / "executar.bat").resolve()

    missing = [
        str(path.name)
        for path in (exe_path, launcher_path)
        if not path.exists()
    ]
    if missing:
        missing_text = ", ".join(missing)
        raise SmokeCheckError(
            f"Artifacts obrigatorios ausentes no dist: {missing_text}"
        )

    _run_command(
        [str(exe_path), "--help"],
        step_name="Luanny.exe --help",
        cwd=dist_path,
        timeout_seconds=timeout_seconds,
    )

    _run_command(
        ["cmd", "/c", str(launcher_path)],
        step_name="executar.bat fluxo [2]->[3]",
        cwd=dist_path,
        timeout_seconds=timeout_seconds,
        input_text="2\n\n3\n",
    )

    if run_regression_tests:
        root = Path(repo_root) if repo_root is not None else Path.cwd()
        python_cmd = str(python_executable or sys.executable)
        _run_command(
            [python_cmd, "-m", "pytest", "-q"],
            step_name="pytest -q",
            cwd=root,
            timeout_seconds=regression_timeout_seconds,
        )


def _run_command(
    command: list[str],
    *,
    step_name: str,
    cwd: Path,
    timeout_seconds: int,
    input_text: str | None = None,
) -> None:
    """Execute one smoke command and normalize errors."""
    print(f"[smoke] Iniciando: {step_name}")
    try:
        subprocess.run(
            command,
            check=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            input=input_text,
        )
    except subprocess.TimeoutExpired as exc:
        raise SmokeCheckError(
            f"Timeout no smoke check '{step_name}' apos {timeout_seconds}s."
        ) from exc
    except subprocess.CalledProcessError as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        raise SmokeCheckError(
            (
                f"Falha no smoke check '{step_name}' "
                f"(exit code={exc.returncode}).\n"
                f"stdout:\n{stdout}\n"
                f"stderr:\n{stderr}"
            )
        ) from exc

    print(f"[smoke] OK: {step_name}")
