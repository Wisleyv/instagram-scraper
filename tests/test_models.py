"""
Testes dos modelos Pydantic — valida serialização, deserialização
e tolerância a campos opcionais.
"""

from __future__ import annotations

from datetime import date, datetime, timezone

import pytest

from luanny.models import (
    AltTextSource,
    AppConfig,
    AriaLabel,
    CollectionMetadata,
    CollectionResult,
    Evidence,
    MediaItem,
    MediaType,
    PostError,
    PostRecord,
    PostType,
    VideoAnalysis,
)


class TestPostRecord:
    """Testes do modelo central PostRecord."""

    def test_minimal_post_record(self) -> None:
        """PostRecord com apenas campos obrigatórios deve ser válido."""
        record = PostRecord(
            post_id="ABC123",
            post_url="https://www.instagram.com/p/ABC123/",
            profile_username="govbr",
        )
        assert record.post_id == "ABC123"
        assert record.post_type == PostType.UNKNOWN
        assert record.caption is None
        assert record.hashtags == []
        assert record.media == []
        assert record.errors == []
        assert record.scraped_at is not None

    def test_full_post_record(self) -> None:
        """PostRecord com todos os campos preenchidos."""
        record = PostRecord(
            post_id="XYZ789",
            post_url="https://www.instagram.com/p/XYZ789/",
            profile_username="govbr",
            caption="Texto de teste #PraTodosVerem",
            hashtags=["#PraTodosVerem"],
            mentions=["@usuario"],
            post_type=PostType.IMAGE,
            is_video=False,
            is_carousel=False,
            media=[
                MediaItem(
                    media_index=0,
                    media_type=MediaType.IMAGE,
                    alt_text="Descrição da imagem",
                    alt_text_source=AltTextSource.MANUAL,
                    is_auto_generated_alt=False,
                ),
            ],
            aria_labels=[
                AriaLabel(
                    tag_name="img",
                    role="img",
                    aria_label="Foto do palácio do governo",
                ),
            ],
            has_audio_description_textual_hint=False,
            accessibility_tags_found=["#PraTodosVerem"],
        )
        assert record.caption == "Texto de teste #PraTodosVerem"
        assert len(record.media) == 1
        assert record.media[0].alt_text_source == AltTextSource.MANUAL
        assert len(record.aria_labels) == 1

    def test_post_record_serialization_roundtrip(self) -> None:
        """PostRecord serializa para JSON e deserializa de volta."""
        original = PostRecord(
            post_id="RT001",
            post_url="https://www.instagram.com/p/RT001/",
            profile_username="govbr",
            caption="Teste de serialização",
            post_type=PostType.CAROUSEL,
            is_carousel=True,
            media=[
                MediaItem(media_index=0, media_type=MediaType.IMAGE, alt_text="Slide 1"),
                MediaItem(media_index=1, media_type=MediaType.IMAGE, alt_text="Slide 2"),
            ],
        )
        json_str = original.model_dump_json()
        restored = PostRecord.model_validate_json(json_str)

        assert restored.post_id == original.post_id
        assert restored.post_type == PostType.CAROUSEL
        assert len(restored.media) == 2
        assert restored.media[1].alt_text == "Slide 2"

    def test_post_record_with_errors(self) -> None:
        """PostRecord com erros parciais permanece válido."""
        record = PostRecord(
            post_id="ERR001",
            post_url="https://www.instagram.com/p/ERR001/",
            profile_username="govbr",
            caption="Legenda OK",
            errors=[
                PostError(
                    field="alt_text",
                    error_type="TimeoutError",
                    message="Timeout ao buscar alt text",
                ),
                PostError(
                    field="aria_labels",
                    error_type="SelectorNotFound",
                    message="Seletor de aria-label não encontrado",
                ),
            ],
        )
        assert len(record.errors) == 2
        assert record.errors[0].field == "alt_text"
        assert record.caption == "Legenda OK"  # Outros campos OK apesar de erros


class TestEvidence:
    """Testes do modelo de evidência com reprodutibilidade."""

    def test_evidence_has_reproducibility_fields(self) -> None:
        """Evidence deve conter todos os campos de reprodutibilidade."""
        evidence = Evidence(
            post_url="https://www.instagram.com/p/TEST/",
            profile_url="https://www.instagram.com/govbr/",
            screenshot_path="evidence/TEST/screenshot.png",
            html_path="evidence/TEST/page.html",
            screenshot_hash="abc123def456",
            html_hash="789ghi012jkl",
            collector_version="0.1.0",
            browser_language="pt-BR",
            viewport_size="1280x720",
        )
        assert evidence.post_url.startswith("https://")
        assert evidence.profile_url.endswith("/govbr/")
        assert evidence.collector_version == "0.1.0"
        assert evidence.browser_language == "pt-BR"
        assert evidence.captured_at is not None

    def test_evidence_serialization_roundtrip(self) -> None:
        """Evidence serializa e deserializa preservando todos os campos."""
        original = Evidence(
            post_url="https://www.instagram.com/p/TEST/",
            profile_url="https://www.instagram.com/govbr/",
            collector_version="0.1.0",
        )
        json_str = original.model_dump_json()
        restored = Evidence.model_validate_json(json_str)
        assert restored.post_url == original.post_url
        assert restored.captured_at is not None


class TestCollectionMetadata:
    """Testes do modelo de metadados da execução."""

    def test_metadata_has_uuid(self) -> None:
        """CollectionMetadata gera UUID automaticamente."""
        meta = CollectionMetadata(
            target_profile="govbr",
            profile_url="https://www.instagram.com/govbr/",
            collector_version="0.1.0",
            max_posts_requested=30,
        )
        assert meta.collection_id is not None
        assert len(meta.collection_id) == 36  # UUID format

    def test_metadata_statistics(self) -> None:
        """CollectionMetadata rastreia estatísticas de coleta."""
        meta = CollectionMetadata(
            target_profile="govbr",
            profile_url="https://www.instagram.com/govbr/",
            collector_version="0.1.0",
            max_posts_requested=30,
            posts_discovered=25,
            posts_collected=22,
            posts_failed=2,
            posts_partial=1,
        )
        assert meta.posts_discovered == 25
        assert meta.posts_collected + meta.posts_failed + meta.posts_partial == 25


class TestCollectionResult:
    """Testes do resultado consolidado."""

    def test_collection_result_serialization(self) -> None:
        """CollectionResult completo serializa para JSON."""
        result = CollectionResult(
            metadata=CollectionMetadata(
                target_profile="govbr",
                profile_url="https://www.instagram.com/govbr/",
                collector_version="0.1.0",
                max_posts_requested=5,
                started_at=datetime.now(timezone.utc),
            ),
            posts=[
                PostRecord(
                    post_id="P001",
                    post_url="https://www.instagram.com/p/P001/",
                    profile_username="govbr",
                ),
            ],
        )
        json_str = result.model_dump_json(indent=2)
        assert '"target_profile": "govbr"' in json_str
        assert '"post_id": "P001"' in json_str

        # Roundtrip
        restored = CollectionResult.model_validate_json(json_str)
        assert len(restored.posts) == 1
        assert restored.metadata.target_profile == "govbr"


class TestMediaItem:
    """Testes do modelo de item de mídia."""

    def test_media_item_minimal(self) -> None:
        """MediaItem com apenas índice é válido."""
        item = MediaItem(media_index=0)
        assert item.media_type == MediaType.UNKNOWN
        assert item.alt_text is None
        assert item.alt_text_source == AltTextSource.UNKNOWN

    def test_media_item_with_auto_alt(self) -> None:
        """MediaItem com alt text auto-gerado."""
        item = MediaItem(
            media_index=0,
            media_type=MediaType.IMAGE,
            alt_text="Foto de Governo do Brasil em 2026",
            alt_text_source=AltTextSource.AUTO_GENERATED,
            is_auto_generated_alt=True,
        )
        assert item.is_auto_generated_alt is True
        assert item.alt_text_source == AltTextSource.AUTO_GENERATED


class TestVideoAnalysis:
    """Testes do modelo de análise de vídeo."""

    def test_v1_video_analysis(self) -> None:
        """VideoAnalysis v1 com apenas campos heurísticos."""
        analysis = VideoAnalysis(
            has_captions_visual_hint=True,
            has_audio_description_textual_hint=False,
        )
        assert analysis.has_captions_visual_hint is True
        assert analysis.transcript is None  # v2 field
        assert analysis.ad_likelihood is None  # v2 field


class TestAppConfig:
    """Testes do modelo de configuração."""

    def test_valid_config(self) -> None:
        """AppConfig com valores válidos."""
        config = AppConfig(
            instagram_username="test",
            instagram_password="test123",
        )
        assert config.max_posts == 30  # default
        assert config.browser_language == "pt-BR"
        assert config.headless is True

    def test_config_validation_max_posts(self) -> None:
        """AppConfig rejeita max_posts fora do range."""
        with pytest.raises(Exception):  # ValidationError
            AppConfig(
                instagram_username="test",
                instagram_password="test123",
                max_posts=0,  # mínimo é 1
            )

    def test_config_with_overrides(self) -> None:
        """AppConfig aceita valores customizados."""
        config = AppConfig(
            instagram_username="test",
            instagram_password="test123",
            max_posts=50,
            headless=False,
            delay_min=5.0,
            delay_max=10.0,
        )
        assert config.max_posts == 50
        assert config.headless is False
        assert config.delay_min == 5.0

    def test_config_with_temporal_window(self) -> None:
        """AppConfig aceita janela temporal válida."""
        config = AppConfig(
            instagram_username="test",
            instagram_password="test123",
            since=date(2026, 1, 1),
            until=date(2026, 12, 31),
            resume=False,
        )

        assert config.since == date(2026, 1, 1)
        assert config.until == date(2026, 12, 31)
        assert config.resume is False

    def test_config_rejects_invalid_temporal_window(self) -> None:
        """AppConfig rejeita when since > until."""
        with pytest.raises(Exception):  # ValidationError
            AppConfig(
                instagram_username="test",
                instagram_password="test123",
                since=date(2026, 12, 31),
                until=date(2026, 1, 1),
            )
