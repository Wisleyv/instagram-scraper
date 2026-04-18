"""Script de build para gerar o executável Windows.

Usa o arquivo Luanny.spec como fonte única de verdade para manter o
empacotamento reproduzível e reduzir divergência entre build script
e configuração do PyInstaller.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
DOCS_DIR = ROOT_DIR / "docs"


def _resolve_playwright_cache_dir() -> Path:
    """Resolve o diretório de cache de browsers do Playwright."""
    env_value = os.getenv("PLAYWRIGHT_BROWSERS_PATH", "").strip()
    if env_value and env_value != "0":
        return Path(env_value).expanduser()

    local_app_data = os.getenv("LOCALAPPDATA")
    if local_app_data:
        return Path(local_app_data) / "ms-playwright"

    return Path.home() / ".cache" / "ms-playwright"


def _required_playwright_browser_folders(package_dir: Path) -> dict[str, str]:
    """Lê browsers.json e retorna pastas mínimas exigidas para Chromium."""
    browsers_json_path = package_dir / "browsers.json"
    if not browsers_json_path.exists():
        raise RuntimeError(
            "Arquivo browsers.json do Playwright não encontrado no pacote "
            f"gerado: {browsers_json_path}"
        )

    payload = json.loads(browsers_json_path.read_text(encoding="utf-8"))
    revisions: dict[str, str] = {}

    for item in payload.get("browsers", []):
        name = str(item.get("name", "")).strip()
        revision = str(item.get("revision", "")).strip()
        if not name or not revision:
            continue
        if name in {
            "chromium",
            "chromium-headless-shell",
            "ffmpeg",
            "winldd",
        }:
            revisions[name] = revision

    required = {
        "chromium": "",
        "chromium-headless-shell": "",
    }
    missing_meta = [name for name in required if name not in revisions]
    if missing_meta:
        raise RuntimeError(
            "Versões obrigatórias não encontradas em browsers.json: "
            f"{', '.join(missing_meta)}"
        )

    folder_map = {
        "chromium": f"chromium-{revisions['chromium']}",
        "chromium-headless-shell": (
            "chromium_headless_shell-"
            f"{revisions['chromium-headless-shell']}"
        ),
    }

    if "ffmpeg" in revisions:
        folder_map["ffmpeg"] = f"ffmpeg-{revisions['ffmpeg']}"
    if "winldd" in revisions:
        folder_map["winldd"] = f"winldd-{revisions['winldd']}"

    return folder_map


def _install_playwright_chromium_if_needed(cache_dir: Path) -> None:
    """Instala Chromium no cache padrão quando necessário."""
    print(
        "Cache do Playwright sem browsers mínimos. "
        "Executando playwright install chromium..."
    )
    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        check=True,
        cwd=ROOT_DIR,
    )


def _ensure_bundled_playwright_browsers(dist_dir: Path) -> None:
    """Garante browsers do Playwright dentro do pacote PyInstaller."""
    package_dir = dist_dir / "_internal" / "playwright" / "driver" / "package"
    if not package_dir.exists():
        raise RuntimeError(
            "Pacote interno do Playwright não encontrado em dist: "
            f"{package_dir}"
        )

    folder_map = _required_playwright_browser_folders(package_dir)
    cache_dir = _resolve_playwright_cache_dir()

    required_folders = [
        folder_map["chromium"],
        folder_map["chromium-headless-shell"],
    ]
    if not all((cache_dir / folder).exists() for folder in required_folders):
        _install_playwright_chromium_if_needed(cache_dir)

    missing_after_install = [
        folder
        for folder in required_folders
        if not (cache_dir / folder).exists()
    ]
    if missing_after_install:
        raise RuntimeError(
            "Browsers obrigatórios ainda ausentes após install: "
            f"{', '.join(missing_after_install)}. "
            f"Cache verificado: {cache_dir}"
        )

    target_root = package_dir / ".local-browsers"
    if target_root.exists():
        shutil.rmtree(target_root)
    target_root.mkdir(parents=True, exist_ok=True)

    copied_folders: list[str] = []
    for _, folder_name in folder_map.items():
        source = cache_dir / folder_name
        if not source.exists():
            continue
        shutil.copytree(source, target_root / folder_name)
        copied_folders.append(folder_name)

    chromium_candidates = [
        target_root / folder_map["chromium"] / "chrome-win64" / "chrome.exe",
        target_root / folder_map["chromium"] / "chrome-win" / "chrome.exe",
    ]
    headless_shell_exe = (
        target_root
        / folder_map["chromium-headless-shell"]
        / "chrome-headless-shell-win64"
        / "chrome-headless-shell.exe"
    )
    missing_exec: list[str] = []
    if not any(path.exists() for path in chromium_candidates):
        missing_exec.append("chromium chrome.exe (chrome-win64/chrome-win)")
    if not headless_shell_exe.exists():
        missing_exec.append(str(headless_shell_exe))
    if missing_exec:
        raise RuntimeError(
            "Pacote ficou sem executáveis do Playwright esperados: "
            f"{'; '.join(missing_exec)}"
        )

    print(
        "Browsers do Playwright incluídos no pacote: "
        f"{', '.join(sorted(copied_folders))}"
    )


def _parse_args() -> argparse.Namespace:
    """Parse command-line options for build and smoke checks."""
    parser = argparse.ArgumentParser(
        description="Build do executavel Luanny para Windows.",
    )
    parser.add_argument(
        "--skip-smoke-checks",
        action="store_true",
        help="Nao executa smoke checks de distribuicao ao final do build.",
    )
    parser.add_argument(
        "--run-regression-tests",
        action="store_true",
        help="Executa pytest -q apos os smoke checks de distribuicao.",
    )
    parser.add_argument(
        "--smoke-timeout",
        type=int,
        default=60,
        help="Timeout (segundos) para cada comando de smoke check.",
    )
    parser.add_argument(
        "--regression-timeout",
        type=int,
        default=1200,
        help="Timeout (segundos) para a etapa opcional de pytest.",
    )
    parser.add_argument(
        "--skip-zip",
        action="store_true",
        help="Nao gera o pacote final zipado de release.",
    )
    parser.add_argument(
        "--release-tag",
        default="windows-test",
        help="Sufixo textual para o nome do zip de release.",
    )
    return parser.parse_args()


def _resolve_version() -> str:
    """Resolve a versao da aplicacao a partir do pacote fonte."""
    if str(SRC_DIR) not in sys.path:
        sys.path.insert(0, str(SRC_DIR))

    try:
        from luanny import __version__
    except Exception:
        return "0.0.0"

    return __version__


def _write_launcher(dist_dir: Path) -> None:
    """Cria o launcher executar.bat no diretório de distribuição."""
    exec_bat = dist_dir / "executar.bat"
    exec_bat.write_text(
        "@echo off\n"
        "setlocal EnableExtensions\n"
        "title Luanny\n"
        "set \"APP_DIR=%~dp0\"\n"
        "set \"APP_EXE=%APP_DIR%Luanny.exe\"\n"
        "\n"
        "if not exist \"%APP_EXE%\" (\n"
        "  echo [ERRO] Nao foi encontrado o executavel em:\n"
        "  echo   %APP_EXE%\n"
        "  echo Verifique se o arquivo Luanny.exe esta na mesma pasta\n"
        "  echo deste .bat.\n"
        "  pause\n"
        "  exit /b 1\n"
        ")\n"
        "\n"
        ":menu\n"
        "cls\n"
        "echo ======================================================\n"
        "echo   Luanny - Launcher Windows\n"
        "echo ======================================================\n"
        "echo [1] Iniciar coleta (modo guiado)\n"
        "echo [2] Mostrar ajuda de comandos\n"
        "echo [3] Sair\n"
        "echo [4] Executar comando avancado\n"
        "echo.\n"
        "choice /c 1234 /n /m \"Escolha uma opcao [1-4]: \"\n"
        "if errorlevel 4 goto avancado\n"
        "if errorlevel 3 goto sair\n"
        "if errorlevel 2 goto ajuda\n"
        "if errorlevel 1 goto coleta\n"
        "\n"
        ":coleta\n"
        "echo.\n"
        "echo Iniciando coleta...\n"
        "echo Dica: durante a coleta, pressione Ctrl+C para interromper.\n"
        "\"%APP_EXE%\" scrape\n"
        "set \"EXIT_CODE=%ERRORLEVEL%\"\n"
        "goto pos_execucao\n"
        "\n"
        ":ajuda\n"
        "echo.\n"
        "\"%APP_EXE%\" --help\n"
        "set \"EXIT_CODE=%ERRORLEVEL%\"\n"
        "goto pos_execucao\n"
        "\n"
        ":avancado\n"
        "echo.\n"
        "echo Digite argumentos para o Luanny.exe.\n"
        "echo Exemplos:\n"
        "echo   --help\n"
        "echo   scrape --profile govbr --max-posts 10\n"
        "echo Durante a execucao: Ctrl+C interrompe o comando atual.\n"
        "echo.\n"
        "set /p \"USER_ARGS=Luanny.exe \"\n"
        "if \"%USER_ARGS%\"==\"\" goto menu\n"
        "\"%APP_EXE%\" %USER_ARGS%\n"
        "set \"EXIT_CODE=%ERRORLEVEL%\"\n"
        "goto pos_execucao\n"
        "\n"
        ":pos_execucao\n"
        "echo.\n"
        "if not \"%EXIT_CODE%\"==\"0\" (\n"
        "  echo [ERRO] O Luanny encerrou com codigo %EXIT_CODE%.\n"
        "  echo Use [2] para ajuda rapida ou [4] para comando avancado.\n"
        ") else (\n"
        "  echo Operacao concluida.\n"
        ")\n"
        "echo.\n"
        "pause\n"
        "goto menu\n"
        "\n"
        ":sair\n"
        "echo Encerrando launcher...\n"
        "endlocal\n"
        "exit /b 0\n",
        encoding="utf-8",
    )


def _write_release_guides(dist_dir: Path, version: str) -> None:
    """Cria guias textuais de uso para publico nao tecnico."""
    readme = dist_dir / "LEIA-ME.txt"
    readme.write_text(
        "LUANNY - COLETOR DE ACESSIBILIDADE INSTAGRAM\n"
        "===========================================\n\n"
        f"Versao para testes: {version}\n\n"
        "ARQUIVOS IMPORTANTES NESTA PASTA:\n"
        "- executar.bat (abrir este arquivo)\n"
        "- Luanny.exe (executavel principal)\n"
        "- MODELO.env (modelo para configurar usuario/senha)\n"
        "- PASSO-A-PASSO.txt (guia detalhado)\n\n"
        "RECOMENDACAO:\n"
        "- Use sempre o executar.bat.\n"
        "- Evite abrir Luanny.exe por clique duplo direto.\n",
        encoding="utf-8",
    )

    steps = dist_dir / "PASSO-A-PASSO.txt"
    steps.write_text(
        "PASSO A PASSO - PRIMEIRA EXECUCAO (WINDOWS)\n"
        "===========================================\n\n"
        "1) DESCOMPACTAR O PACOTE ZIP\n"
        "   - Extraia o arquivo zip em uma pasta simples, por exemplo:\n"
        "     C:\\LuannyTeste\\\n\n"
        "2) CONFIGURAR CREDENCIAIS DO INSTAGRAM\n"
        "   - Na pasta extraida, localize o arquivo MODELO.env.\n"
        "   - Faça uma copia dele e renomeie a copia para .env\n"
        "   - Abra o arquivo .env e preencha:\n"
        "       INSTAGRAM_USERNAME=seu_usuario\n"
        "       INSTAGRAM_PASSWORD=sua_senha\n"
        "   - Salve e feche.\n\n"
        "3) INICIAR O LUANNY\n"
        "   - Dê duplo clique em executar.bat\n"
        "   - Escolha a opcao [1] para iniciar coleta guiada\n"
        "   - Siga as perguntas exibidas na tela\n\n"
        "   - Quantidade de posts: recomendado ate 50 por rodada\n"
        "   - Limite tecnico maximo: 500 por rodada\n"
        "   - A qualquer momento, Ctrl+C interrompe a coleta\n\n"
        "4) LOGIN NO NAVEGADOR\n"
        "   - Se solicitado, faça login no Instagram na janela aberta\n"
        "   - Essa janela e o navegador de automacao, nao uma GUI do Luanny\n"
        "   - Volte para a janela do launcher e aguarde a coleta\n\n"
        "5) RESULTADOS\n"
        "   - Ao final, os arquivos ficam na pasta data\\...\n"
        "   - Principais saidas:\n"
        "       posts.json\n"
        "       summary.csv\n"
        "       report.md\n"
        "       manifest.json\n\n"
        "6) SE ALGO DER ERRADO\n"
        "   - Rode a opcao [2] no launcher para ver ajuda\n"
        "   - Para comandos manuais, use a opcao [4]\n"
        "   - Confirme se o arquivo .env esta preenchido\n"
        "   - Se persistir, compartilhe a pasta logs\\ para suporte\n",
        encoding="utf-8",
    )

    notes = dist_dir / "RELEASE_NOTES.txt"
    notes.write_text(
        "LUANNY - RELEASE DE TESTES\n"
        "==========================\n\n"
        f"Versao: {version}\n"
        f"Gerado em: {datetime.now().isoformat(timespec='seconds')}\n\n"
        "Conteudo desta release:\n"
        "- Executavel Windows atualizado\n"
        "- Launcher executar.bat\n"
        "- Browsers Playwright (Chromium) embutidos no pacote\n"
        "- Modelo de configuracao MODELO.env\n"
        "- Guia de uso passo a passo\n"
        "- Smoke checks de distribuicao validados no build\n",
        encoding="utf-8",
    )


def _copy_release_assets(dist_dir: Path) -> None:
    """Copia arquivos auxiliares para facilitar uso em ambiente de testes."""
    env_example = ROOT_DIR / ".env.example"
    if env_example.exists():
        shutil.copyfile(env_example, dist_dir / "MODELO.env")

    usage_doc = DOCS_DIR / "USAGE.md"
    if usage_doc.exists():
        shutil.copyfile(usage_doc, dist_dir / "GUIA_USO.md")

    install_doc = DOCS_DIR / "INSTALL.md"
    if install_doc.exists():
        shutil.copyfile(install_doc, dist_dir / "GUIA_INSTALACAO.md")


def _create_release_zip(
    dist_dir: Path,
    *,
    version: str,
    release_tag: str,
) -> Path:
    """Gera um zip de release contendo a pasta completa dist/Luanny."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_tag = release_tag.strip().replace(" ", "-") or "windows-test"
    zip_base = ROOT_DIR / "dist" / f"Luanny-v{version}-{safe_tag}-{timestamp}"

    archive_path = shutil.make_archive(
        base_name=str(zip_base),
        format="zip",
        root_dir=str(dist_dir.parent),
        base_dir=dist_dir.name,
    )
    return Path(archive_path)


def main() -> None:
    args = _parse_args()
    version = _resolve_version()

    print("Iniciando build do Luanny...")

    # 1. Limpar pastas de build antigas
    for folder in [ROOT_DIR / "build", ROOT_DIR / "dist"]:
        if folder.exists():
            shutil.rmtree(folder)

    # 2. PyInstaller build usando o spec como fonte única de verdade
    print("Construindo executável Windows...")
    spec_path = ROOT_DIR / "Luanny.spec"
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        str(spec_path),
        "--noconfirm",
        "--clean",
        f"--distpath={ROOT_DIR / 'dist'}",
        f"--workpath={ROOT_DIR / 'build'}",
    ]

    subprocess.run(cmd, check=True, cwd=ROOT_DIR)

    print("Luanny construído com sucesso em dist/Luanny/")

    # 3. Preparar artefatos de release em dist/Luanny
    dist_dir = ROOT_DIR / "dist" / "Luanny"
    dist_dir.mkdir(parents=True, exist_ok=True)
    _ensure_bundled_playwright_browsers(dist_dir)
    _write_launcher(dist_dir)
    _copy_release_assets(dist_dir)
    _write_release_guides(dist_dir, version)

    if args.skip_smoke_checks:
        print(
            "Smoke checks de distribuicao foram ignorados "
            "(--skip-smoke-checks)."
        )
    else:
        if str(SRC_DIR) not in sys.path:
            sys.path.insert(0, str(SRC_DIR))

        from luanny.build_smoke import run_windows_distribution_smoke_checks

        print("Executando smoke checks de distribuicao (Fase 5)...")
        run_windows_distribution_smoke_checks(
            dist_dir,
            timeout_seconds=args.smoke_timeout,
            run_regression_tests=args.run_regression_tests,
            regression_timeout_seconds=args.regression_timeout,
            repo_root=ROOT_DIR,
            python_executable=sys.executable,
        )
        print("Smoke checks concluidos com sucesso.")

    if args.skip_zip:
        print("Pacote zip nao gerado (--skip-zip).")
    else:
        zip_path = _create_release_zip(
            dist_dir,
            version=version,
            release_tag=args.release_tag,
        )
        print(f"Pacote de release gerado: {zip_path}")

    print("Build concluido! Artefatos atualizados em dist/Luanny")


if __name__ == "__main__":
    main()
