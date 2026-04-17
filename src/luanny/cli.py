"""
CLI do Luanny — ponto de entrada da aplicação.

Implementa o comando principal `scrape` usando Typer.
Quando invocado sem argumentos, entra em modo interativo guiado.
"""

from __future__ import annotations

from typing import Annotated, Optional

import typer
from rich.console import Console

from luanny import __version__

app = typer.Typer(
    name="luanny",
    help="Luanny — Coletor de dados de acessibilidade do Instagram para pesquisa acadêmica.",
    no_args_is_help=False,
    rich_markup_mode="rich",
)

console = Console()


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"Luanny v{__version__}")
        raise typer.Exit()


def _interactive_prompt() -> dict[str, object]:
    """Modo interativo: pergunta parâmetros ao usuário com defaults sensatos."""
    console.print(
        "\n[bold cyan]╔══════════════════════════════════════════════════════╗[/]"
        "\n[bold cyan]║[/]     [bold white]Luanny — Coletor de Acessibilidade[/]            [bold cyan]║[/]"
        "\n[bold cyan]╚══════════════════════════════════════════════════════╝[/]\n"
    )

    profile = typer.prompt("  Perfil do Instagram (ex: govbr)")
    max_posts = typer.prompt("  Quantidade máxima de posts", default=30, type=int)
    headless_str = typer.prompt("  Executar sem interface gráfica? (S/N)", default="S")
    headless = headless_str.strip().upper() in ("S", "SIM", "Y", "YES")

    return {
        "profile": profile,
        "max_posts": max_posts,
        "headless": headless,
        "capture_evidence": True,
    }


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[
        Optional[bool],
        typer.Option("--version", "-V", callback=_version_callback, is_eager=True,
                     help="Exibir versão do Luanny."),
    ] = None,
) -> None:
    """Luanny — Coletor de dados de acessibilidade do Instagram."""
    if ctx.invoked_subcommand is None:
        # Sem subcomando: mostrar ajuda
        console.print(
            f"\n  [bold]Luanny[/] v{__version__} — "
            "Coletor de dados de acessibilidade do Instagram\n"
            "\n  Use [bold cyan]luanny scrape[/] para iniciar uma coleta."
            "\n  Use [bold cyan]luanny --help[/] para ver todas as opções.\n"
        )


@app.command()
def scrape(
    profile: Annotated[
        Optional[str],
        typer.Option("--profile", "-p", help="Username do perfil-alvo no Instagram."),
    ] = None,
    max_posts: Annotated[
        Optional[int],
        typer.Option("--max-posts", "-n", help="Quantidade máxima de posts a coletar."),
    ] = None,
    headless: Annotated[
        Optional[bool],
        typer.Option("--headless/--headed", help="Executar browser sem/com interface gráfica."),
    ] = None,
    capture_evidence: Annotated[
        Optional[bool],
        typer.Option("--capture-evidence/--no-evidence",
                     help="Capturar evidências técnicas por post."),
    ] = None,
    output_dir: Annotated[
        Optional[str],
        typer.Option("--output-dir", "-o", help="Diretório de saída dos resultados."),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Exibir logs detalhados."),
    ] = False,
) -> None:
    """Inicia a coleta de dados de acessibilidade de um perfil do Instagram."""
    from luanny.log import setup_logging

    setup_logging(verbose=verbose)

    # Se perfil não foi passado, entrar em modo interativo
    if profile is None:
        params = _interactive_prompt()
        profile = params["profile"]
        max_posts = max_posts or params.get("max_posts", 30)
        headless = headless if headless is not None else params.get("headless", True)
        capture_evidence = capture_evidence if capture_evidence is not None else True

    # Montar overrides de config a partir dos argumentos CLI
    cli_overrides: dict[str, object] = {}
    if max_posts is not None:
        cli_overrides["max_posts"] = max_posts
    if headless is not None:
        cli_overrides["headless"] = headless
    if capture_evidence is not None:
        cli_overrides["capture_evidence"] = capture_evidence
    if output_dir is not None:
        cli_overrides["output_dir"] = output_dir

    # Carregar config (falha cedo se credenciais ausentes)
    from luanny.config import load_config

    config = load_config(**cli_overrides)

    # Executar pipeline
    from luanny.orchestrator import run_collection

    run_collection(profile=profile, config=config)
