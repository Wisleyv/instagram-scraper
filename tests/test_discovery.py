"""
Testes do módulo profile_discovery — Fase 2.

Testa a lógica de navegação num perfil, rolagem simulada do grid
e extração dos identificadores a partir das URLs.
"""

from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock, call

import pytest

from luanny.models import AppConfig
from luanny.profile_discovery import discover_posts


@pytest.fixture()
def mock_config() -> AppConfig:
    """Config de teste para discovery."""
    return AppConfig(
        instagram_username="test_user",
        instagram_password="test_pass",
        max_posts=5,
        headless=True,
    )


@pytest.fixture()
def mock_session(mock_config):
    """Cria um BrowserSession mockado."""
    session = MagicMock()
    session.config = mock_config
    session.page = MagicMock()
    return session


class TestProfileDiscovery:
    """Testes da descoberta de posts."""

    def test_discover_posts_vazio(self, mock_session, mock_config, monkeypatch):
        """Deve retornar vazio se nenhum post for encontrado e o fim da página for alcançado."""
        # Fix: Mock time.sleep e human_delay_sync para os testes rodarem rápido
        monkeypatch.setattr("time.sleep", MagicMock())
        monkeypatch.setattr("luanny.browser.human_delay_sync", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_cookie_banner", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_post_login_dialogs", MagicMock())

        # Configura o mock do locator para retornar vazio
        mock_locator = MagicMock()
        mock_locator.all.return_value = []
        mock_session.page.locator.return_value = mock_locator

        # Eval da rolagem (simulando altura de página que não muda)
        mock_session.page.evaluate.return_value = 1000

        result = discover_posts(mock_session, "https://instagram.com/test", mock_config)

        assert result == []

    def test_discover_posts_com_limite(self, mock_session, mock_config, monkeypatch):
        """Deve extrair os IDs corretamente, parando quando atingir max_posts."""
        monkeypatch.setattr("time.sleep", MagicMock())
        monkeypatch.setattr("luanny.browser.human_delay_sync", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_cookie_banner", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_post_login_dialogs", MagicMock())

        # Vamos simular a página retornando 3 elementos na primeira rolagem, e mais 3 na segunda
        el1 = MagicMock()
        el1.get_attribute.return_value = "/p/POST_1/"
        el2 = MagicMock()
        el2.get_attribute.return_value = "/reel/REEL_1/"
        el3 = MagicMock()
        el3.get_attribute.return_value = "/p/POST_2/"
        el4 = MagicMock()
        el4.get_attribute.return_value = "/p/POST_3/"
        el5 = MagicMock()
        el5.get_attribute.return_value = "/p/POST_4/"
        el6 = MagicMock()
        el6.get_attribute.return_value = "/p/POST_5/"

        mock_locator = MagicMock()
        # side_effect retorna listas sequenciais em cada chamada de .all()
        # Mas dentro do loop itera por seletores_to_try.
        # Digamos que na primeira vez (.all() do primeiro seletor) ele retorne 3 elementos
        mock_locator.all.side_effect = [
            [el1, el2, el3],  # Primeira rolagem, primeiro seletor
            [el3, el4, el5, el6],  # Segunda rolagem, encontra duplicado + novos
        ]
        mock_session.page.locator.return_value = mock_locator

        # Simulando alturas de página simulando scroll
        mock_session.page.evaluate.side_effect = [
            1000, # new_height
            None, # window.scrollTo
            2000, # current_height
            2000, # new_height
            None, # window.scrollTo
            3000, # current_height
        ]

        result = discover_posts(mock_session, "https://instagram.com/test", mock_config)

        # Configuramos max_posts=5 no mock_config
        assert len(result) == 5
        assert result[0] == ("POST_1", "https://www.instagram.com/p/POST_1/")
        assert result[1] == ("REEL_1", "https://www.instagram.com/reel/REEL_1/")
        assert result[2] == ("POST_2", "https://www.instagram.com/p/POST_2/")
        assert result[3] == ("POST_3", "https://www.instagram.com/p/POST_3/")
        assert result[4] == ("POST_4", "https://www.instagram.com/p/POST_4/")

    def test_discover_posts_com_invalidos(self, mock_session, mock_config, monkeypatch):
        """Deve ignorar elementos sem href ou que não se encaixam no padrão /p/ ou /reel/."""
        monkeypatch.setattr("time.sleep", MagicMock())
        monkeypatch.setattr("luanny.browser.human_delay_sync", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_cookie_banner", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_post_login_dialogs", MagicMock())

        el_invalid1 = MagicMock()
        el_invalid1.get_attribute.return_value = None
        el_invalid2 = MagicMock()
        el_invalid2.get_attribute.return_value = "/about/"
        el_valid = MagicMock()
        el_valid.get_attribute.return_value = "/p/VALID/"

        mock_locator = MagicMock()
        mock_locator.all.return_value = [el_invalid1, el_invalid2, el_valid]
        mock_session.page.locator.return_value = mock_locator

        # Fim do perfil na primeira tentativa
        mock_session.page.evaluate.return_value = 1000

        result = discover_posts(mock_session, "https://instagram.com/test", mock_config)

        assert len(result) == 1
        assert result[0] == ("VALID", "https://www.instagram.com/p/VALID/")

    def test_discover_posts_skip_seen_ids_and_collect_older(
        self,
        mock_session,
        monkeypatch,
    ):
        """Em resume, deve ignorar vistos e seguir até achar novos."""
        monkeypatch.setattr("time.sleep", MagicMock())
        monkeypatch.setattr("luanny.browser.human_delay_sync", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_cookie_banner", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_post_login_dialogs", MagicMock())

        config = AppConfig(
            instagram_username="test_user",
            instagram_password="test_pass",
            max_posts=2,
            headless=True,
        )

        el_s1 = MagicMock()
        el_s1.get_attribute.return_value = "/p/SEEN_1/"
        el_s2 = MagicMock()
        el_s2.get_attribute.return_value = "/p/SEEN_2/"
        el_n1 = MagicMock()
        el_n1.get_attribute.return_value = "/p/NEW_1/"
        el_n2 = MagicMock()
        el_n2.get_attribute.return_value = "/reel/NEW_2/"

        mock_locator = MagicMock()
        mock_locator.all.side_effect = [
            [el_s1, el_s2],
            [el_s1, el_s2],
            [el_s2, el_n1, el_n2],
        ]
        mock_session.page.locator.return_value = mock_locator
        mock_session.page.evaluate.return_value = 1000

        result = discover_posts(
            mock_session,
            "https://instagram.com/test",
            config,
            seen_post_ids={"SEEN_1", "SEEN_2"},
        )

        assert result == [
            ("NEW_1", "https://www.instagram.com/p/NEW_1/"),
            ("NEW_2", "https://www.instagram.com/reel/NEW_2/"),
        ]

    def test_discover_posts_stops_when_since_boundary_is_reached(
        self,
        mock_session,
        monkeypatch,
    ):
        """Com since, interrompe discovery quando os itens visíveis já são antigos."""
        monkeypatch.setattr("time.sleep", MagicMock())
        monkeypatch.setattr("luanny.browser.human_delay_sync", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_cookie_banner", MagicMock())
        monkeypatch.setattr("luanny.auth._dismiss_post_login_dialogs", MagicMock())

        config = AppConfig(
            instagram_username="test_user",
            instagram_password="test_pass",
            max_posts=5,
            headless=True,
            since=date(2026, 4, 10),
        )

        def make_dated_element(href: str, datetime_value: str) -> MagicMock:
            element = MagicMock()

            def get_attribute(name: str):
                if name == "href":
                    return href
                if name == "datetime":
                    return datetime_value
                return None

            element.get_attribute.side_effect = get_attribute
            return element

        old_1 = make_dated_element("/p/OLD_1/", "2026-04-01T10:00:00Z")
        old_2 = make_dated_element("/p/OLD_2/", "2026-04-02T10:00:00Z")
        old_3 = make_dated_element("/reel/OLD_3/", "2026-04-03T10:00:00Z")

        mock_locator = MagicMock()
        mock_locator.all.side_effect = [
            [old_1, old_2],
            [old_1, old_2],
            [old_2, old_3],
            [old_2, old_3],
        ]
        mock_session.page.locator.return_value = mock_locator
        mock_session.page.evaluate.return_value = 1000

        result = discover_posts(mock_session, "https://instagram.com/test", config)

        assert result == []
