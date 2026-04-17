"""
Módulo centralizado de seletores CSS/XPath do Instagram.

Todos os seletores usados para interagir com o DOM do Instagram
devem estar definidos aqui. Nenhum seletor deve ser hardcoded
nos módulos de extração ou descoberta.

Cada seletor possui uma estratégia primária e fallbacks.
Quando o Instagram muda sua interface, apenas este arquivo
precisa ser atualizado.

STUB — Fase 0: seletores preliminares. Validação real na Fase 2.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Selector:
    """Seletor com estratégia primária e fallbacks."""
    primary: str
    fallbacks: tuple[str, ...] = ()
    description: str = ""


# ---------------------------------------------------------------------------
# Seletores de autenticação
# ---------------------------------------------------------------------------

LOGIN_USERNAME_INPUT = Selector(
    primary='input[name="username"]',
    description="Campo de username na tela de login",
)

LOGIN_PASSWORD_INPUT = Selector(
    primary='input[name="password"]',
    description="Campo de senha na tela de login",
)

LOGIN_SUBMIT_BUTTON = Selector(
    primary='button[type="submit"]',
    description="Botão de submit no formulário de login",
)

# ---------------------------------------------------------------------------
# Seletores de perfil e grid
# ---------------------------------------------------------------------------

PROFILE_POSTS_GRID = Selector(
    primary="a[href*='/p/'], a[href*='/reel/']",
    fallbacks=("article a[href*='/p/'], article a[href*='/reel/']",),
    description="Links de posts no grid do perfil principal",
)

# ---------------------------------------------------------------------------
# Seletores de post individual
# ---------------------------------------------------------------------------

POST_CAPTION = Selector(
    primary="main span[dir='auto']",
    fallbacks=("main div[dir='auto']", "main span"),
    description="Texto da legenda do post",
)

POST_CAPTION_MORE_BUTTON = Selector(
    primary="main button:has-text('mais'), main button:has-text('more')",
    description="Botão 'mais/more' para expandir legenda",
)

POST_IMAGE = Selector(
    primary="main img[src*='instagram']",
    fallbacks=("main img",),
    description="Imagem principal do post",
)

POST_VIDEO = Selector(
    primary="main video",
    description="Vídeo do post",
)

POST_CAROUSEL_NEXT = Selector(
    primary="main button[aria-label*='Avançar'], main button[aria-label*='Next']",
    description="Botão avançar do carrossel (bilíngue pt/en)",
)

POST_CAROUSEL_INDICATOR = Selector(
    primary="main div[role='tablist']",
    fallbacks=("main div._acnb",),
    description="Indicador de slides do carrossel",
)

POST_ARIA_LABELS = Selector(
    primary="main [aria-label]",
    description="Todos os elementos com aria-label dentro do post",
)

# ---------------------------------------------------------------------------
# Seletores de detecção de bloqueio
# ---------------------------------------------------------------------------

CHALLENGE_PAGE = Selector(
    primary="#challenge, form[data-testid='challenge']",
    fallbacks=("div:has-text('atividade suspeita'), div:has-text('suspicious activity')",),
    description="Página de checkpoint/challenge do Instagram",
)


# ---------------------------------------------------------------------------
# Padrões de texto (para heurísticas de alt text auto-gerado)
# ---------------------------------------------------------------------------

# Padrões que indicam alt text gerado automaticamente pelo Instagram
AUTO_ALT_PATTERNS_PT = (
    "Foto de",
    "Pode conter:",
    "A imagem pode conter",
    "Nenhuma descrição de foto disponível",
)

AUTO_ALT_PATTERNS_EN = (
    "Photo by",
    "May contain:",
    "Image may contain",
    "No photo description available",
)

AUTO_ALT_PATTERNS = AUTO_ALT_PATTERNS_PT + AUTO_ALT_PATTERNS_EN

# Hashtags de acessibilidade a detectar no caption
ACCESSIBILITY_HASHTAGS = (
    "#pratodosverem",
    "#pracegover",
    "#pratodomundover",
    "#audiodescrição",
    "#audiodescricao",
    "#imagemacessivel",
    "#acessibilidade",
    "#acessibilidadedigital",
    "#descrevaimagem",
)
