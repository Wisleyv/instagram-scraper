"""
Módulo de extração de dados do post.

Abre cada post em sua própria página e extrai todos os dados
de acessibilidade previstos no schema PostRecord.
"""

from __future__ import annotations

import re
import time
from datetime import datetime, timezone
from typing import TYPE_CHECKING, List

from luanny.log import get_logger
from luanny.models import (
    AltTextSource,
    AppConfig,
    MediaItem,
    MediaType,
    PostRecord,
    PostType,
    AriaLabel,
)
from luanny.selectors import (
    POST_CAPTION,
    POST_CAPTION_MORE_BUTTON,
    POST_IMAGE,
    POST_VIDEO,
    POST_CAROUSEL_NEXT,
    POST_CAROUSEL_INDICATOR,
    POST_ARIA_LABELS,
    AUTO_ALT_PATTERNS_PT,
    AUTO_ALT_PATTERNS_EN,
)

if TYPE_CHECKING:
    from luanny.browser import BrowserSession

logger = get_logger("post_extractor")

def _extract_hashtags_and_mentions(text: str) -> tuple[List[str], List[str]]:
    """Extrai listas de hashtags e menções de um texto."""
    hashtags = re.findall(r"(#\w+)", text)
    mentions = re.findall(r"(@\w+)", text)
    return hashtags, mentions

def _is_auto_generated_alt(alt_text: str) -> bool:
    """Verifica se o alt text parece ser gerado automaticamente pelo Instagram."""
    if not alt_text:
        return False
        
    alt_lower = alt_text.lower()
    
    # Checar padrões em inglês e português
    for pattern in AUTO_ALT_PATTERNS_EN + AUTO_ALT_PATTERNS_PT:
        if pattern.lower() in alt_lower:
            return True
            
    # Checar se começa com certas strings comuns de ia
    if alt_lower.startswith("photo by") or alt_lower.startswith("foto de") or "may be an image of" in alt_lower:
        return True
        
    return False

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from playwright.sync_api import Error as PlaywrightError

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1.5, min=2, max=10),
    retry=retry_if_exception_type(PlaywrightError),
    reraise=True
)
def extract_post(
    session: BrowserSession,
    post_id: str,
    post_url: str,
    profile_username: str,
    config: AppConfig,
) -> PostRecord:
    """
    Extrai dados de acessibilidade de um post individual.

    Abre a página do post, extrai caption, mídia, alt text,
    ARIA labels e sinais de acessibilidade.

    Args:
        session: Sessão do browser Playwright.
        post_id: ID do post no Instagram.
        post_url: URL canônica do post.
        profile_username: Username do perfil-alvo.
        config: Configuração da aplicação.

    Returns:
        PostRecord com todos os dados extraídos (ou parciais em caso de erro).
    """
    logger.info("extractor_started", post_id=post_id, url=post_url)
    page = session.page
    
    # 1. Navegar até o post
    try:
        page.goto(post_url, wait_until="load", timeout=config.navigation_timeout)
        time.sleep(3.0)  # Aguardar renderização React
    except Exception as e:
        logger.error("extractor_navigation_error", error=str(e), post_id=post_id)
        
        # (5.4) Captura de evidência de erro em caso de falha brutal na rede
        try:
            str_ts = str(int(time.time()))
            page.screenshot(path=f"evidence_error_{post_id}_{str_ts}.png")
        except:
            pass
            
        raise
        
    # Verificar erro 404 (página não existe)
    if "Page Not Found" in page.title() or "Página não encontrada" in page.title():
        logger.warning("extractor_page_not_found", post_id=post_id)

    # 2. Clicar no botão 'mais/more' para expandir legenda, se houver
    try:
        more_btn = page.query_selector(POST_CAPTION_MORE_BUTTON.primary)
        if more_btn and more_btn.is_visible():
            more_btn.click()
            time.sleep(1.0)
    except Exception as e:
        logger.debug("extractor_no_more_btn", error=str(e))

    # 3. Extrair Caption (Legenda)
    caption_text = ""
    selectors_caption = [POST_CAPTION.primary] + list(POST_CAPTION.fallbacks)
    for sel in selectors_caption:
        elements = page.locator(sel).all()
        # Pegar todos os spans válidos ou div de legenda
        valid_texts = []
        for el in elements:
            try:
                text = el.inner_text().strip()
                if text and len(text) > 10 and text != profile_username:
                    valid_texts.append(text)
            except Exception:
                continue
        if valid_texts:
            caption_text = "\n".join(valid_texts)
            break
            
    # Extrair hashtags e menções
    hashtags, mentions = _extract_hashtags_and_mentions(caption_text)

    # 4. Avaliar tipo de Mídia
    is_video = page.query_selector(POST_VIDEO.primary) is not None
    is_carousel = False
    
    selectors_carousel = [POST_CAROUSEL_INDICATOR.primary] + list(POST_CAROUSEL_INDICATOR.fallbacks)
    for sel in selectors_carousel:
        if page.query_selector(sel):
            is_carousel = True
            break
            
    post_type = PostType.CAROUSEL if is_carousel else (PostType.VIDEO if is_video else PostType.IMAGE)

    # 5. Extração de mídias (Alt Texts)
    media_items: List[MediaItem] = []
    
    # Como as vezes o carousel não move (ou botões faltam), coletamos as imagens principais visíveis
    selectors_img = [POST_IMAGE.primary] + list(POST_IMAGE.fallbacks)
    img_elements = []
    for sel in selectors_img:
        elements = page.locator(sel).all()
        if elements:
            img_elements = elements
            break
            
    for i, img in enumerate(img_elements):
        try:
            alt_attr = img.get_attribute("alt") or ""
            # Pula imagens prováveis de profile e ícones
            if "profile picture" in alt_attr.lower() or "foto do perfil" in alt_attr.lower():
                continue
                
            is_auto = _is_auto_generated_alt(alt_attr)
            source = AltTextSource.AUTO_GENERATED if is_auto else (AltTextSource.MANUAL if alt_attr else AltTextSource.ABSENT)
            
            item = MediaItem(
                media_index=len(media_items),
                media_type=MediaType.IMAGE,
                alt_text=alt_attr,
                alt_text_source=source,
                is_auto_generated_alt=is_auto,
            )
            media_items.append(item)
            
            if not is_carousel and len(media_items) == 1:
                break # Pega apenas a primeira imagem substancial se não for carrossel
        except Exception:
            continue
            
    if is_video and len(media_items) == 0:
        # Se for video puro
        media_items.append(MediaItem(
            media_index=0,
            media_type=MediaType.VIDEO,
            alt_text="",
            alt_text_source=AltTextSource.ABSENT,
            is_auto_generated_alt=False
        ))

    # 6. Extração de ARIA e ferramentas estruturais
    aria_labels: List[AriaLabel] = []
    try:
        aria_elements = page.locator(POST_ARIA_LABELS.primary).all()
        for el in aria_elements:
            try:
                label = el.get_attribute("aria-label")
                role = el.get_attribute("role") or "button"
                if label:
                    # Tentar deduzir o tag_name usando evaluate pode ser lento. Usamos "element" como fallback.
                    # Mas tentamos manter compatibilidade com o schema.
                    aria_labels.append(AriaLabel(
                        tag_name="element",
                        role=role,
                        aria_label=label,
                        context_hint="post_interactive"
                    ))
            except Exception as e:
                logger.debug("invalid_aria_label", error=str(e))
                continue
    except Exception as e:
        logger.debug("extractor_aria_error", error=str(e))

    # Construir o Record
    record = PostRecord(
        post_id=post_id,
        post_url=post_url,
        profile_username=profile_username,
        scraped_at=datetime.now(timezone.utc),
        caption=caption_text,
        hashtags=hashtags,
        mentions=mentions,
        post_type=post_type,
        is_video=is_video,
        is_carousel=is_carousel,
        media=media_items,
        aria_labels=aria_labels,
    )
    
    logger.info("extractor_finished", post_id=post_id, media_found=len(media_items))
    return record
