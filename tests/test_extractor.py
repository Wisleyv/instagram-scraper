"""
Testes do módulo post_extractor — Fase 3.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from luanny.models import AppConfig, PostType, AltTextSource, MediaType
from luanny.post_extractor import extract_post, _is_auto_generated_alt


@pytest.fixture()
def mock_config() -> AppConfig:
    """Config de teste para extractor."""
    return AppConfig(
        instagram_username="test_user",
        instagram_password="test_pass",
        headless=True,
    )


@pytest.fixture()
def mock_session(mock_config):
    """Cria um BrowserSession mockado."""
    session = MagicMock()
    session.config = mock_config
    session.page = MagicMock()
    return session


def test_is_auto_generated_alt():
    assert _is_auto_generated_alt("Photo by Governo do Brasil") is True
    assert _is_auto_generated_alt("May be an image of text") is True
    assert _is_auto_generated_alt("Pode ser uma foto de cachorro") is True
    assert _is_auto_generated_alt("Um belo cachorro na praia") is False
    assert _is_auto_generated_alt("") is False


def test_extract_post_image(mock_session, mock_config, monkeypatch):
    """Testa a extração de uma imagem simples."""
    monkeypatch.setattr("time.sleep", MagicMock())
    
    # Mock do título
    mock_session.page.title.return_value = "Instagram"
    
    # Mock do botão 'more'
    mock_session.page.query_selector.side_effect = lambda sel: None  # Simulando ausências isoladas
    
    # Simulando 1 div sendo o carousel nulo e 0 videos, mas 1 imagem real
    # Nós temos 4 query_selectors em extract_post: more_btn, video, carousel (vários fallbacks)
    def fake_query_selector(selector):
        if "video" in selector: return None
        if "tablist" in selector or "_acnb" in selector: return None
        return None
    mock_session.page.query_selector.side_effect = fake_query_selector

    # Mocks para .all() nos locators (captions, imagens e arias)
    def fake_locator(selector):
        mock_loc = MagicMock()
        if "span" in selector:
            # caption
            el = MagicMock()
            el.inner_text.return_value = "Esta é uma legenda de teste com #hashtag e @mencao #pratodosverem."
            mock_loc.all.return_value = [el]
        elif "img" in selector:
            el = MagicMock()
            el.get_attribute.return_value = "May be an image of text"
            mock_loc.all.return_value = [el]
        elif "aria-label" in selector:
            el = MagicMock()
            el.get_attribute.side_effect = lambda attr: "Like" if attr == "aria-label" else "button"
            mock_loc.all.return_value = [el]
        else:
            mock_loc.all.return_value = []
        return mock_loc
        
    mock_session.page.locator.side_effect = fake_locator

    record = extract_post(
        mock_session, "POST123", "https://instagram.com/p/POST123", "test_user", mock_config
    )

    assert record.post_id == "POST123"
    assert record.post_type == PostType.IMAGE
    assert len(record.hashtags) == 2
    assert "#hashtag" in record.hashtags
    assert len(record.mentions) == 1
    assert "@mencao" in record.mentions
    
    assert len(record.media) == 1
    assert record.media[0].is_auto_generated_alt is True
    # Era CAPTION_DESCRIBED, agora volta para AUTO_GENERATED ou o comportamento correto do is_auto.
    assert record.media[0].alt_text_source == AltTextSource.AUTO_GENERATED
    
    assert len(record.aria_labels) == 1
    assert record.aria_labels[0].aria_label == "Like"


def test_extract_post_video(mock_session, mock_config, monkeypatch):
    """Testa a extração de um vídeo."""
    monkeypatch.setattr("time.sleep", MagicMock())
    
    mock_session.page.title.return_value = "Video Post"
    
    def fake_query_selector(selector):
        if "video" in selector: 
            el = MagicMock()
            return el
        return None
    mock_session.page.query_selector.side_effect = fake_query_selector

    def fake_locator(selector):
        mock_loc = MagicMock()
        mock_loc.all.return_value = []
        return mock_loc
        
    mock_session.page.locator.side_effect = fake_locator

    record = extract_post(
        mock_session, "VID123", "https://instagram.com/reel/VID123", "test_user", mock_config
    )

    assert record.post_id == "VID123"
    assert record.post_type == PostType.VIDEO
    assert record.is_video is True
    assert len(record.media) == 1
    assert record.media[0].media_type == MediaType.VIDEO
    assert record.media[0].alt_text_source == AltTextSource.ABSENT
