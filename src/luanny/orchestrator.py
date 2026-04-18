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

from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from luanny import __version__
from luanny.log import get_logger
from luanny.models import (
    AppConfig,
    CollectionState,
    CollectionMetadata,
    CollectionResult,
    PostRecord,
)
from luanny.runtime_paths import resolve_runtime_path

logger = get_logger("orchestrator")


def _filter_posts_by_publication_window(
    posts: list[PostRecord],
    since: date | None,
    until: date | None,
) -> tuple[list[PostRecord], int, int]:
    """Filtra posts por janela temporal com tolerância a datas ausentes."""
    if since is None and until is None:
        return posts, 0, 0

    filtered: list[PostRecord] = []
    dropped_by_window = 0
    missing_publication_date = 0

    for post in posts:
        if post.published_at is None:
            missing_publication_date += 1
            filtered.append(post)
            continue

        post_date = post.published_at.date()
        if since is not None and post_date < since:
            dropped_by_window += 1
            continue
        if until is not None and post_date > until:
            dropped_by_window += 1
            continue

        filtered.append(post)

    return filtered, dropped_by_window, missing_publication_date


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
        since=config.since,
        until=config.until,
        resume_enabled=config.resume,
    )

    from luanny.execution_manifest import (
        create_audit_event,
        write_execution_manifest,
    )

    audit_trail: list[dict[str, Any]] = []

    def _audit(step: str, status: str, **details: object) -> None:
        audit_trail.append(
            create_audit_event(step, status, **details)
        )

    _audit(
        "collection_start",
        "started",
        profile=profile,
        max_posts=config.max_posts,
        headless=config.headless,
        capture_evidence=config.capture_evidence,
        resume=config.resume,
        since=config.since,
        until=config.until,
    )

    dropped_by_window = 0
    missing_publication_date = 0
    state_path: Path | None = None
    state_after: CollectionState | None = None
    run_dir: Path | None = None

    from luanny.collection_state import (
        load_collection_state,
        save_collection_state,
        update_collection_state,
    )

    if config.resume:
        state = load_collection_state(profile, config.output_dir)
        state_before = state.model_copy(deep=True)
        _audit(
            "state_load",
            "completed",
            resume_enabled=True,
            known_post_ids=len(state.seen_post_ids),
        )
    else:
        state = CollectionState(profile=profile)
        state_before = None
        logger.info(
            "collection_state_resume_disabled",
            profile=profile,
        )
        _audit(
            "state_load",
            "skipped",
            resume_enabled=False,
            reason="resume_disabled",
        )

    logger.info(
        "coleta_iniciada",
        profile=profile,
        max_posts=config.max_posts,
        headless=config.headless,
    )

    # --- Etapa 1: Inicializar browser ---
    from luanny.browser import create_browser_context, close_browser_context

    logger.info("etapa_browser", status="iniciando")
    session = create_browser_context(config)
    logger.info("etapa_browser", status="concluída")
    _audit("browser", "completed", headless=config.headless)

    try:
        # --- Etapa 2: Autenticação ---
        from luanny.auth import ensure_authenticated

        logger.info("etapa_auth", status="iniciando")
        ensure_authenticated(session, config)
        logger.info("etapa_auth", status="concluída")
        _audit("auth", "completed")

        # --- Etapa 3: Descoberta de postagens ---
        from luanny.profile_discovery import discover_posts

        logger.info("etapa_discovery", status="iniciando", profile=profile)
        seen_post_ids = set(state.seen_post_ids) if config.resume else set()
        discovered_posts = discover_posts(
            session,
            profile_url,
            config,
            seen_post_ids=seen_post_ids,
        )

        post_urls = discovered_posts

        metadata.posts_discovered = len(post_urls)
        logger.info(
            "etapa_discovery",
            status="concluída",
            posts_encontrados=len(post_urls),
            modo_resume=config.resume,
            ids_previamente_vistos=len(seen_post_ids),
        )
        _audit(
            "discovery",
            "completed",
            posts_discovered=len(post_urls),
            known_post_ids=len(seen_post_ids),
        )

        # --- Etapa 4: Extração de dados por post ---
        from luanny.post_extractor import extract_post
        from luanny.browser import human_delay_sync
        from rich.progress import (
            BarColumn,
            Progress,
            SpinnerColumn,
            TaskProgressColumn,
            TextColumn,
        )

        posts = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            transient=True,
        ) as progress:
            task_ext = progress.add_task(
                f"[cyan]Extraindo posts de @{profile}...",
                total=len(post_urls),
            )

            for i, (post_id, post_url) in enumerate(post_urls):
                logger.debug(
                    "etapa_extração",
                    post=f"{i + 1}/{len(post_urls)}",
                    post_id=post_id,
                )

                # (5.3) Rate Limiting dinâmico configurável para evitar
                # Action Block da Meta
                if i > 0:
                    logger.debug(
                        "rate_limiting",
                        msg=(
                            f"Aguardando entre {config.delay_min} "
                            f"e {config.delay_max}s"
                        ),
                    )
                    human_delay_sync(config.delay_min, config.delay_max)

                record = extract_post(
                    session,
                    post_id,
                    post_url,
                    profile,
                    config,
                )
                posts.append(record)
                progress.advance(task_ext)

        _audit("extraction", "completed", posts_extracted=len(posts))

        posts, dropped_by_window, missing_publication_date = (
            _filter_posts_by_publication_window(
                posts,
                config.since,
                config.until,
            )
        )
        _audit(
            "temporal_filter",
            "completed",
            posts_after_filter=len(posts),
            posts_dropped_by_window=dropped_by_window,
            posts_missing_publication_date=missing_publication_date,
        )
        if dropped_by_window > 0 or missing_publication_date > 0:
            logger.info(
                "etapa_filtro_temporal",
                since=config.since,
                until=config.until,
                posts_mantidos=len(posts),
                posts_descartados=dropped_by_window,
                posts_sem_data_publicacao=missing_publication_date,
            )

        timestamp_str = metadata.started_at.strftime("%Y%m%d_%H%M%S")
        run_dir = (
            resolve_runtime_path(config.output_dir)
            / f"{profile}_{timestamp_str}"
        )

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
                task_ev = progress.add_task(
                    "[magenta]Capturando Evidências (Screenshots/HTML)...",
                    total=len(posts),
                )
                for record in posts:
                    capture_evidence(
                        session,
                        record,
                        config,
                        base_output_dir=run_dir,
                    )
                    progress.advance(task_ev)
            logger.info("etapa_evidência", status="concluída")
            _audit(
                "evidence",
                "completed",
                capture_evidence=True,
                posts_with_evidence=len(posts),
            )
        else:
            _audit(
                "evidence",
                "skipped",
                capture_evidence=False,
            )

        # --- Etapa 6: Contabilizar resultados ---
        # Recalcular métricas finais de posts baseados no array final
        metadata.posts_collected = sum(1 for p in posts if not p.errors)
        metadata.posts_failed = sum(
            1 for p in posts if p.errors and p.caption is None and not p.media
        )
        metadata.posts_partial = sum(
            1
            for p in posts
            if p.errors and (p.caption is not None or bool(p.media))
        )
        metadata.finished_at = datetime.now(timezone.utc)

        result = CollectionResult(metadata=metadata, posts=posts)

        # --- Etapa 7: Exportação ---
        from luanny.exporters import export_results

        logger.info("etapa_exportação", status="iniciando")
        export_results(result, config, base_output_dir=run_dir)
        logger.info("etapa_exportação", status="concluída")
        _audit(
            "export",
            "completed",
            run_dir=run_dir,
        )

        if config.resume:
            state = update_collection_state(
                state=state,
                posts=posts,
                collection_id=metadata.collection_id,
            )
            state_path = save_collection_state(state, config.output_dir)
            state_after = state.model_copy(deep=True)
            logger.info(
                "etapa_estado",
                status="concluída",
                path=str(state_path),
                posts_conhecidos=len(state.seen_post_ids),
            )
            _audit(
                "state_save",
                "completed",
                state_path=state_path,
                known_post_ids=len(state.seen_post_ids),
            )
        else:
            logger.info(
                "etapa_estado",
                status="ignorada",
                motivo="resume_desativado",
            )
            _audit(
                "state_save",
                "skipped",
                reason="resume_disabled",
            )

        _audit(
            "manifest",
            "completed",
            output_path=run_dir / "manifest.json",
        )
        manifest_path = write_execution_manifest(
            run_dir=run_dir,
            metadata=metadata,
            config=config,
            state_before=state_before,
            state_after=state_after,
            state_path=state_path,
            dropped_by_window=dropped_by_window,
            missing_publication_date=missing_publication_date,
            audit_trail=audit_trail,
        )
        logger.info(
            "etapa_manifesto",
            status="concluída",
            path=str(manifest_path),
        )

        _audit(
            "collection_finish",
            "completed",
            posts_collected=metadata.posts_collected,
            posts_failed=metadata.posts_failed,
            posts_partial=metadata.posts_partial,
        )

    except Exception as exc:
        _audit(
            "collection_finish",
            "failed",
            error_type=type(exc).__name__,
            message=str(exc),
        )
        logger.error(
            "coleta_falhou",
            error_type=type(exc).__name__,
            error=str(exc),
        )
        raise

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
