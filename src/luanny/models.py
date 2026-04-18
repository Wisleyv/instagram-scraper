"""
Modelos de dados do Projeto Luanny.

Este módulo define todos os contratos de dados utilizados pelo sistema.
Todos os módulos devem comunicar-se exclusivamente via estes tipos —
nunca via dicts soltos.

Os modelos são definidos com Pydantic v2 para validação e serialização.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, model_validator


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class PostType(str, Enum):
    """Tipo de postagem do Instagram."""
    IMAGE = "image"
    VIDEO = "video"
    CAROUSEL = "carousel"
    UNKNOWN = "unknown"


class AltTextSource(str, Enum):
    """Origem do texto alternativo da imagem."""
    MANUAL = "manual"            # Alt text definido pelo autor
    AUTO_GENERATED = "auto"      # Alt text gerado pelo Instagram
    ABSENT = "absent"            # Nenhum alt text presente
    UNKNOWN = "unknown"          # Não foi possível determinar


class MediaType(str, Enum):
    """Tipo de mídia individual em um post."""
    IMAGE = "image"
    VIDEO = "video"
    UNKNOWN = "unknown"


# ---------------------------------------------------------------------------
# Sub-modelos: mídia, ARIA, vídeo, evidência, erro
# ---------------------------------------------------------------------------

class MediaItem(BaseModel):
    """Representa um item de mídia individual dentro de um post."""
    media_index: int = Field(description="Índice da mídia no post (0-based)")
    media_type: MediaType = Field(default=MediaType.UNKNOWN, description="Tipo da mídia")
    src: Optional[str] = Field(default=None, description="URL da mídia, quando disponível")
    alt_text: Optional[str] = Field(default=None, description="Texto alternativo da imagem")
    alt_text_source: AltTextSource = Field(
        default=AltTextSource.UNKNOWN,
        description="Origem do alt text (manual, auto, ausente)",
    )
    is_auto_generated_alt: Optional[bool] = Field(
        default=None,
        description="Se o alt text foi gerado automaticamente pelo Instagram",
    )
    poster: Optional[str] = Field(default=None, description="URL do poster de vídeo")
    dimensions: Optional[str] = Field(
        default=None, description="Dimensões da mídia (ex: '1080x1080'), quando disponível"
    )


class AriaLabel(BaseModel):
    """Representa um elemento com aria-label encontrado no DOM do post."""
    tag_name: str = Field(description="Nome da tag HTML (ex: 'button', 'img')")
    role: Optional[str] = Field(default=None, description="Atributo role do elemento")
    aria_label: str = Field(description="Valor do aria-label")
    context_hint: Optional[str] = Field(
        default=None,
        description="Contexto adicional sobre a posição ou função do elemento",
    )


class VideoAnalysis(BaseModel):
    """Análise de vídeo — v1 contém apenas heurísticas textuais."""
    has_captions_visual_hint: Optional[bool] = Field(
        default=None,
        description="Se há indício visual de legendas (ícone/botão de CC)",
    )
    has_audio_description_textual_hint: Optional[bool] = Field(
        default=None,
        description="Se a legenda do post menciona audiodescrição",
    )
    # Campos para v2 (módulo de áudio):
    transcript: Optional[str] = Field(default=None, description="Transcrição via Whisper (v2)")
    ad_likelihood: Optional[float] = Field(
        default=None, description="Probabilidade de audiodescrição (v2)"
    )
    keywords_found: Optional[list[str]] = Field(
        default=None, description="Palavras-chave de AD encontradas (v2)"
    )
    audio_processing_error: Optional[str] = Field(
        default=None, description="Erro no processamento de áudio (v2)"
    )


class Evidence(BaseModel):
    """Evidência técnica de coleta, com metadados de reprodutibilidade científica."""
    post_url: str = Field(description="URL canônica do post coletado")
    profile_url: str = Field(description="URL do perfil-alvo")
    screenshot_path: Optional[str] = Field(
        default=None, description="Caminho relativo do screenshot PNG"
    )
    html_path: Optional[str] = Field(
        default=None, description="Caminho relativo do HTML salvo"
    )
    screenshot_hash: Optional[str] = Field(
        default=None, description="SHA-256 do arquivo de screenshot"
    )
    html_hash: Optional[str] = Field(
        default=None, description="SHA-256 do HTML salvo"
    )
    captured_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Data/hora da captura (ISO 8601 com fuso horário)",
    )
    collector_version: str = Field(description="Versão do software coletor")
    browser_language: str = Field(default="pt-BR", description="Idioma configurado no browser")
    viewport_size: str = Field(default="1280x720", description="Dimensões do viewport")


class PostError(BaseModel):
    """Erro não-fatal ocorrido durante a extração de um post."""
    field: str = Field(description="Campo ou etapa que falhou (ex: 'caption', 'alt_text')")
    error_type: str = Field(description="Tipo do erro (ex: 'TimeoutError', 'SelectorNotFound')")
    message: str = Field(description="Mensagem de erro legível")
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Quando o erro ocorreu",
    )


# ---------------------------------------------------------------------------
# Modelo principal: PostRecord
# ---------------------------------------------------------------------------

class PostRecord(BaseModel):
    """
    Registro completo de dados extraídos de uma postagem do Instagram.

    Este é o modelo central do sistema. Cada post coletado gera exatamente
    um PostRecord. Campos podem ser None quando a extração falha parcialmente.
    """
    # Identificação
    post_id: str = Field(description="ID único do post no Instagram")
    post_url: str = Field(description="URL canônica do post")
    profile_username: str = Field(description="Username do perfil-alvo")

    # Temporalidade
    scraped_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Data/hora da coleta (ISO 8601 com fuso horário)",
    )
    published_at: Optional[datetime] = Field(
        default=None,
        description="Data/hora de publicação do post no Instagram (ISO 8601)",
    )

    # Conteúdo textual
    caption: Optional[str] = Field(default=None, description="Legenda completa do post")
    hashtags: list[str] = Field(default_factory=list, description="Hashtags encontradas")
    mentions: list[str] = Field(default_factory=list, description="Menções (@usuario) encontradas")

    # Tipo e mídia
    post_type: PostType = Field(default=PostType.UNKNOWN, description="Tipo do post")
    is_video: bool = Field(default=False, description="Se o post contém vídeo")
    is_carousel: bool = Field(default=False, description="Se o post é carrossel")
    media: list[MediaItem] = Field(default_factory=list, description="Itens de mídia do post")

    # Acessibilidade
    aria_labels: list[AriaLabel] = Field(
        default_factory=list, description="Elementos com aria-label no DOM do post"
    )
    has_audio_description_textual_hint: Optional[bool] = Field(
        default=None,
        description="Se a legenda contém marcadores textuais de audiodescrição",
    )
    accessibility_tags_found: list[str] = Field(
        default_factory=list,
        description="Tags de acessibilidade encontradas (ex: #PraTodosVerem, #PraCegoVer)",
    )

    # Análise de vídeo
    video_analysis: Optional[VideoAnalysis] = Field(
        default=None, description="Análise de vídeo (heurística na v1)"
    )

    # Evidência e erros
    evidence: Optional[Evidence] = Field(
        default=None, description="Evidência técnica de coleta"
    )
    errors: list[PostError] = Field(
        default_factory=list, description="Erros não-fatais durante extração deste post"
    )


# ---------------------------------------------------------------------------
# Modelos de contexto: metadados da execução e resultado consolidado
# ---------------------------------------------------------------------------

class CollectionMetadata(BaseModel):
    """Metadados da execução de coleta para reprodutibilidade científica."""
    collection_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="UUID da execução",
    )
    target_profile: str = Field(description="Username do perfil coletado")
    profile_url: str = Field(description="URL completa do perfil")
    started_at: Optional[datetime] = Field(
        default=None, description="Início da execução (ISO 8601 + fuso)"
    )
    finished_at: Optional[datetime] = Field(
        default=None, description="Fim da execução (ISO 8601 + fuso)"
    )
    collector_version: str = Field(description="Versão do software")
    browser_language: str = Field(default="pt-BR", description="Idioma do browser")
    max_posts_requested: int = Field(description="Limite de posts solicitado")
    since: Optional[date] = Field(
        default=None,
        description="Data inicial da janela de coleta (quando configurada)",
    )
    until: Optional[date] = Field(
        default=None,
        description="Data final da janela de coleta (quando configurada)",
    )
    resume_enabled: bool = Field(
        default=True,
        description="Se a execução reaproveitou estado incremental anterior",
    )
    posts_discovered: int = Field(default=0, description="Posts encontrados no grid")
    posts_collected: int = Field(default=0, description="Posts processados com sucesso")
    posts_failed: int = Field(default=0, description="Posts com falha total")
    posts_partial: int = Field(default=0, description="Posts com falha parcial")


class CollectionResult(BaseModel):
    """Resultado consolidado de uma execução completa de coleta."""
    metadata: CollectionMetadata = Field(description="Metadados da execução")
    posts: list[PostRecord] = Field(default_factory=list, description="Posts coletados")


class CollectionState(BaseModel):
    """Estado incremental persistido para evitar retrabalho entre execuções."""
    profile: str = Field(description="Perfil ao qual o estado pertence")
    collection_id: Optional[str] = Field(
        default=None,
        description="Última execução que atualizou este estado",
    )
    seen_post_ids: list[str] = Field(
        default_factory=list,
        description="IDs de posts já coletados com sucesso",
    )
    last_published_at: Optional[datetime] = Field(
        default=None,
        description="Data de publicação mais antiga já coletada",
    )
    last_post_id: Optional[str] = Field(
        default=None,
        description="ID do post associado a last_published_at",
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Momento da última atualização do estado",
    )


# ---------------------------------------------------------------------------
# Modelo de configuração da aplicação
# ---------------------------------------------------------------------------

class AppConfig(BaseModel):
    """Configuração da aplicação, carregada de .env e/ou argumentos CLI."""
    # Credenciais
    instagram_username: str = Field(description="Username da conta operacional")
    instagram_password: str = Field(description="Senha da conta operacional")

    # Parâmetros de coleta
    max_posts: int = Field(default=30, ge=1, le=500, description="Máximo de posts por execução")
    headless: bool = Field(default=True, description="Executar browser sem interface gráfica")
    capture_evidence: bool = Field(default=True, description="Capturar evidências por post")
    browser_language: str = Field(default="pt-BR", description="Idioma do browser")

    # Timeouts (milissegundos)
    navigation_timeout: int = Field(
        default=30_000, ge=5000, description="Timeout de navegação (ms)"
    )
    element_timeout: int = Field(
        default=10_000, ge=2000, description="Timeout de espera por elemento (ms)"
    )

    # Rate limiting
    delay_min: float = Field(default=3.0, ge=1.0, description="Delay mínimo entre ações (s)")
    delay_max: float = Field(default=7.0, ge=2.0, description="Delay máximo entre ações (s)")

    # Janela temporal e retomada incremental
    since: Optional[date] = Field(
        default=None,
        description="Data inicial de interesse (AAAA-MM-DD)",
    )
    until: Optional[date] = Field(
        default=None,
        description="Data final de interesse (AAAA-MM-DD)",
    )
    resume: bool = Field(
        default=True,
        description="Se deve reutilizar estado incremental para deduplicação",
    )

    # Diretórios
    output_dir: str = Field(default="data", description="Diretório base de saída")

    @model_validator(mode="after")
    def _validate_temporal_window(self) -> "AppConfig":
        """Valida consistência da janela temporal configurada."""
        if self.since and self.until and self.since > self.until:
            raise ValueError("since deve ser menor ou igual a until")
        return self
