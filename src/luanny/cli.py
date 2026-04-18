"""
CLI do Luanny — ponto de entrada da aplicação.

Implementa o comando principal `scrape` usando Typer.
Quando invocado sem argumentos, entra em modo interativo guiado.
"""

from __future__ import annotations

import sys
from datetime import date
from typing import Annotated, Optional

import typer
from rich.console import Console

from luanny import __version__

app = typer.Typer(
    name="luanny",
    help=(
        "Luanny — Coletor de dados de acessibilidade do Instagram "
        "para pesquisa acadêmica."
    ),
    no_args_is_help=False,
    rich_markup_mode="rich",
)

console = Console()

DEFAULT_MAX_POSTS = 30
RECOMMENDED_MAX_POSTS = 50
HARD_MAX_POSTS = 500


def _is_frozen_runtime() -> bool:
    """Retorna True quando executando como binário empacotado."""
    return bool(getattr(sys, "frozen", False))


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"Luanny v{__version__}")
        raise typer.Exit()


def _validate_max_posts_value(value: int) -> int:
    """Valida quantidade de posts no intervalo suportado pela aplicação."""
    if value < 1 or value > HARD_MAX_POSTS:
        raise typer.BadParameter(
            f"Informe um valor entre 1 e {HARD_MAX_POSTS} em --max-posts."
        )
    return value


def _prompt_max_posts() -> int:
    """Solicita a quantidade de posts com orientação anti-bloqueio."""
    while True:
        value = typer.prompt(
            f"  Quantidade de posts por rodada [1-{HARD_MAX_POSTS}]",
            default=DEFAULT_MAX_POSTS,
            type=int,
        )

        try:
            max_posts = _validate_max_posts_value(value)
        except typer.BadParameter as exc:
            console.print(f"  [yellow]{exc}[/]")
            continue

        if max_posts > RECOMMENDED_MAX_POSTS:
            console.print(
                "  [yellow]Aviso:[/] acima de "
                f"{RECOMMENDED_MAX_POSTS} posts por rodada "
                "aumenta risco de bloqueio temporário da plataforma."
            )
            if not typer.confirm(
                "  Deseja manter esse valor mesmo assim?",
                default=False,
            ):
                continue

        return max_posts


def _prompt_headless_mode() -> bool:
    """Pergunta se o navegador deve rodar sem janela (headless)."""
    console.print(
        "  Navegador de automação (não é GUI do Luanny):\n"
        "    sem janela = recomendado para coleta\n"
        "    com janela = usar para login/checkpoint/diagnóstico"
    )
    raw = typer.prompt(
        "  Executar sem janela do navegador? (S/N)",
        default="S",
    )
    return raw.strip().upper() in ("S", "SIM", "Y", "YES")


def _prompt_optional_date(label: str) -> date | None:
    """Solicita uma data opcional em formato ISO (AAAA-MM-DD)."""
    while True:
        raw = typer.prompt(label, default="").strip()
        if not raw:
            return None
        try:
            return date.fromisoformat(raw)
        except ValueError:
            console.print(
                "  [yellow]Data inválida. Use o formato AAAA-MM-DD.[/]"
            )


def _parse_optional_date_value(
    value: object,
    *,
    option_name: str,
) -> date | None:
    """Converte valor de data opcional para date com validação amigável."""
    if value is None:
        return None

    if isinstance(value, date):
        return value

    if isinstance(value, str):
        raw = value.strip()
        if not raw:
            return None
        try:
            return date.fromisoformat(raw)
        except ValueError as exc:
            raise typer.BadParameter(
                f"Use AAAA-MM-DD em --{option_name}."
            ) from exc

    raise typer.BadParameter(f"Valor inválido em --{option_name}.")


def _interactive_prompt() -> dict[str, object]:
    """Modo interativo com prompts claros para usuário não técnico."""
    console.print(
        "\n[bold cyan]╔════════════════════════════════════════════"
        "══════════╗[/]"
        "\n[bold cyan]║[/]     [bold white]Luanny — Coletor de "
        "Acessibilidade[/]            [bold cyan]║[/]"
        "\n[bold cyan]╚════════════════════════════════════════════"
        "══════════╝[/]\n"
    )

    console.print(
        "[bold]Critérios recomendados de coleta:[/]\n"
        f"  - Recomendado: até {RECOMMENDED_MAX_POSTS} posts por rodada\n"
        f"  - Limite técnico máximo: {HARD_MAX_POSTS} posts por rodada\n"
        "  - Rodadas menores ajudam a reduzir risco de bloqueio\n"
        "  - Interrupção manual: pressione Ctrl+C a qualquer momento\n"
    )

    profile = typer.prompt("  Perfil do Instagram (ex: govbr)")
    max_posts = _prompt_max_posts()
    headless = _prompt_headless_mode()
    since = _prompt_optional_date("  Data inicial (AAAA-MM-DD, opcional)")
    until = _prompt_optional_date("  Data final (AAAA-MM-DD, opcional)")
    resume_str = typer.prompt(
        "  Retomar estado incremental e deduplicar? (S/N)",
        default="S",
    )
    resume = resume_str.strip().upper() in ("S", "SIM", "Y", "YES")

    return {
        "profile": profile,
        "max_posts": max_posts,
        "headless": headless,
        "since": since,
        "until": until,
        "resume": resume,
        "capture_evidence": True,
    }


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-V",
            callback=_version_callback,
            is_eager=True,
            help="Exibir versão do Luanny.",
        ),
    ] = None,
) -> None:
    """Luanny — Coletor de dados de acessibilidade do Instagram."""
    if ctx.invoked_subcommand is None:
        if _is_frozen_runtime():
            console.print(
                f"\n  [bold]Luanny[/] v{__version__} — "
                "Coletor de dados de acessibilidade do Instagram\n"
            )
            console.print(
                "  [yellow]Esta versão funciona em terminal (CLI), "
                "não em janela GUI nativa do Windows.[/]"
            )
            console.print("  [1] Iniciar coleta (modo guiado)")
            console.print("  [2] Mostrar ajuda")
            console.print("  [3] Sair\n")

            choice = typer.prompt("Selecione uma opção", default="1")
            choice = choice.strip()

            if choice == "1":
                scrape()
            elif choice == "2":
                console.print(ctx.get_help())
            else:
                console.print("Encerrando Luanny.")
            return

        # Sem subcomando em modo Python: mostrar ajuda rápida
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
        typer.Option(
            "--profile",
            "-p",
            help="Username do perfil-alvo no Instagram.",
        ),
    ] = None,
    max_posts: Annotated[
        Optional[int],
        typer.Option(
            "--max-posts",
            "-n",
            help=(
                "Quantidade de posts por rodada. "
                "Recomendado: até 50; máximo: 500."
            ),
        ),
    ] = None,
    headless: Annotated[
        Optional[bool],
        typer.Option(
            "--headless/--headed",
            help=(
                "Modo do navegador de automação "
                "(sem janela/com janela). Não é GUI do Luanny."
            ),
        ),
    ] = None,
    capture_evidence: Annotated[
        Optional[bool],
        typer.Option(
            "--capture-evidence/--no-evidence",
            help="Capturar evidências técnicas por post.",
        ),
    ] = None,
    output_dir: Annotated[
        Optional[str],
        typer.Option(
            "--output-dir",
            "-o",
            help="Diretório de saída dos resultados.",
        ),
    ] = None,
    since: Annotated[
        Optional[str],
        typer.Option("--since", help="Data inicial (AAAA-MM-DD)."),
    ] = None,
    until: Annotated[
        Optional[str],
        typer.Option("--until", help="Data final (AAAA-MM-DD)."),
    ] = None,
    resume: Annotated[
        bool,
        typer.Option(
            "--resume/--no-resume",
            help="Reutilizar estado incremental para deduplicação.",
        ),
    ] = True,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Exibir logs detalhados."),
    ] = False,
) -> None:
    """Inicia a coleta de dados de acessibilidade de um perfil do Instagram."""
    from luanny.log import setup_logging

    setup_logging(verbose=verbose)

    if max_posts is not None:
        max_posts = _validate_max_posts_value(max_posts)

    # Se perfil não foi passado, entrar em modo interativo
    if profile is None:
        params = _interactive_prompt()
        profile = params["profile"]
        max_posts = max_posts or params.get("max_posts", DEFAULT_MAX_POSTS)
        headless = (
            headless if headless is not None else params.get("headless", True)
        )
        capture_evidence = (
            capture_evidence
            if capture_evidence is not None
            else True
        )
        since = since if since is not None else params.get("since")
        until = until if until is not None else params.get("until")
        if resume is True:
            resume = bool(params.get("resume", True))

    parsed_since = _parse_optional_date_value(since, option_name="since")
    parsed_until = _parse_optional_date_value(until, option_name="until")

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
    if parsed_since is not None:
        cli_overrides["since"] = parsed_since
    if parsed_until is not None:
        cli_overrides["until"] = parsed_until
    cli_overrides["resume"] = resume

    # Carregar config (falha cedo se credenciais ausentes)
    from luanny.config import load_config

    config = load_config(**cli_overrides)

    browser_mode = (
        "sem janela (headless)"
        if config.headless
        else "com janela (headed)"
    )
    resume_mode = "ativada" if config.resume else "desativada"
    console.print(
        "\n[bold]Resumo da execução[/]"
        f"\n  Perfil: {profile}"
        f"\n  Posts por rodada: {config.max_posts}"
        f"\n  Navegador: {browser_mode}"
        f"\n  Janela temporal: {config.since or '-'} até {config.until or '-'}"
        f"\n  Retomada incremental: {resume_mode}"
    )
    if config.max_posts > RECOMMENDED_MAX_POSTS:
        console.print(
            "  [yellow]Atenção:[/] volume acima de "
            f"{RECOMMENDED_MAX_POSTS} pode elevar risco de bloqueio."
        )
    console.print(
        "  [cyan]Interrupção manual:[/] pressione Ctrl+C para "
        "parar a coleta.\n"
    )

    # Executar pipeline
    from luanny.orchestrator import run_collection

    try:
        run_collection(profile=profile, config=config)
    except KeyboardInterrupt:
        console.print(
            "\n[yellow]Coleta interrompida pelo usuário (Ctrl+C).[/]"
        )
        raise typer.Exit(code=130)


if __name__ == "__main__":
    app()
