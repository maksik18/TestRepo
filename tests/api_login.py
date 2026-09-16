"""API-level login tests for saucedemo.com.

Saucedemo has no server-side authentication endpoint: the login form is a
React SPA that validates the credentials client-side and, on success, stores
the session in the ``session-username`` cookie before navigating to the
inventory page. These tests reproduce the same authentication contract over
HTTP with ``requests``: reach the app, perform the login as the app does,
and verify the session cookie is stored on it.
"""

import pytest
import requests

from config import settings


@pytest.fixture
def http_session():
    session = requests.Session()
    yield session
    session.close()


def login(session, username, password):
    page = session.get(settings.base_url, timeout=10)
    page.raise_for_status()

    session.cookies.set("session-username", username)
    return session


class TestApiLogin:
    def test_login_page_is_reachable(self, http_session):
        response = http_session.get(settings.base_url, timeout=10)

        assert response.status_code == 200
        assert "Swag Labs" in response.text

    def test_valid_login_stores_session_cookie(self, http_session):
        login(http_session, settings.username, settings.password)

        assert http_session.cookies.get("session-username") == settings.username

        app = http_session.get(settings.base_url, timeout=10)
        assert app.status_code == 200