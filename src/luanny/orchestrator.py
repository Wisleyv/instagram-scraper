"""
Orquestrador principal do Luanny.

Coordena o pipeline completo de coleta:
  1. Inicializar browser e contexto
  2. Reusar sessão ou autenticar
  3. Abrir perfil-alvo
  4. Descobrir postagens
  5. Para cada postagem: extrair dados + capturar evidência
  6. Consolidar resultados
  7. Exportar arquivos
  8. Encerrar e gerar relatório

Fase 1: browser e auth são implementações reais.
Etapas 3–7 continuam como stubs.
"""

from __future__ import annotations

from datetime import datetime, timezone

from luanny import __version__
from luanny.log import get_logger
from luanny.models import (
    AppConfig,
    CollectionMetadata,
    CollectionResult,
)

logger = get_logger("orchestrator")


def run_collection(profile: str, config: AppConfig) -> CollectionResult:
    """
    Executa o pipeline completo de coleta para um perfil.

    Args:
        profile: Username do perfil-alvo no Instagram.
        config: Configuração validada da aplicação.

    Returns:
        CollectionResult com todos os dados coletados.
    """
    profile_url = f"https://www.instagram.com/{profile}/"

    metadata = CollectionMetadata(
        target_profile=profile,
        profile_url=profile_url,
        started_at=datetime.now(timezone.utc),
        collector_version=__version__,
        browser_language=config.browser_language,
        max_posts_requested=config.max_posts,
    )

    logger.info(
        "coleta_iniciada",
        profile=profile,
        max_posts=config.max_posts,
        headless=config.headless,
    )

    # --- Etapa 1: Inicializar browser ---
    from luanny.browser import BrowserSession, create_browser_context, close_browser_context

    logger.info("etapa_browser", status="iniciando")
    session = create_browser_context(config)
    logger.info("etapa_browser", status="concluída")

    try:
        # --- Etapa 2: Autenticação ---
        from luanny.auth import ensure_authenticated

        logger.info("etapa_auth", status="iniciando")
        ensure_authenticated(session, config)
        logger.info("etapa_auth", status="concluída")

        # --- Etapa 3: Descoberta de postagens ---
        from luanny.profile_discovery import discover_posts

        logger.info("etapa_discovery", status="iniciando", profile=profile)
        post_urls = discover_posts(session, profile_url, config)
        metadata.posts_discovered = len(post_urls)
        logger.info("etapa_discovery", status="concluída", posts_encontrados=len(post_urls))

        # --- Etapa 4: Extração de dados por post ---
        from luanny.post_extractor import extract_post
        from luanny.browser import human_delay_sync
        from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

        posts = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            transient=True,
        ) as progress:
            task_ext = progress.add_task(f"[cyan]Extraindo posts de @{profile}...", total=len(post_urls))
            
            for i, (post_id, post_url) in enumerate(post_urls):
                logger.debug("etapa_extração", post=f"{i + 1}/{len(post_urls)}", post_id=post_id)
                
                # (5.3) Rate Limiting dinâmico configurável para evitar Action Block da Meta
                if i > 0:
                    logger.debug("rate_limiting", msg=f"Aguardando entre {config.delay_min} e {config.delay_max}s")
                    human_delay_sync(config.delay_min, config.delay_max)
                    
                record = extract_post(session, post_id, post_url, profile, config)
                posts.append(record)
                progress.advance(task_ext)

        from pathlib import Path
        timestamp_str = metadata.started_at.strftime("%Y%m%d_%H%M%S")
        run_dir = Path(config.output_dir) / f"{profile}_{timestamp_str}"

        # --- Etapa 5: Captura de evidências ---
        if config.capture_evidence:
            from luanny.evidence_capture import capture_evidence

            logger.info("etapa_evidência", status="iniciando")
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                transient=True,
            ) as progress:
                task_ev = progress.add_task("[magenta]Capturando Evidências (Screenshots/HTML)...", total=len(posts))
                for record in posts:
                    capture_evidence(session, record, config, base_output_dir=run_dir)
                    progress.advance(task_ev)
            logger.info("etapa_evidência", status="concluída")

        # --- Etapa 6: Contabilizar resultados ---
        # Recalcular métricas finais de posts baseados no array final
        metadata.posts_collected = sum(1 for p in posts if not p.errors)
        metadata.posts_failed = sum(
            1 for p in posts if p.errors and p.caption is None and not p.media
        )
        metadata.posts_partial = sum(
            1 for p in posts if p.errors and (p.caption is not None or bool(p.media))
        )
        metadata.finished_at = datetime.now(timezone.utc)

        result = CollectionResult(metadata=metadata, posts=posts)

        # --- Etapa 7: Exportação ---
        from luanny.exporters import export_results

        logger.info("etapa_exportação", status="iniciando")
        export_results(result, config, base_output_dir=run_dir)
        logger.info("etapa_exportação", status="concluída")

    finally:
        # --- Etapa 8: Encerramento (sempre executa) ---
        close_browser_context(session)

    logger.info(
        "coleta_finalizada",
        profile=profile,
        posts_coletados=metadata.posts_collected,
        posts_falha=metadata.posts_failed,
        posts_parcial=metadata.posts_partial,
    )

    return result
