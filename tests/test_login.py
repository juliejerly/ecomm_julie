import time

import pytest
from playwright.sync_api import Page, sync_playwright
from pages.login_page import LoginPage


class TestLogin:

    @pytest.fixture
    def isolated_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            yield page
            browser.close()

    @pytest.mark.parametrize("cred_key, expected_result", [
        ("VALID_CREDS", True),
        ("INVALID_CREDS", False)
    ])
    def test_login(self, cred_key, expected_result, isolated_page: Page):
        login_page = LoginPage(isolated_page)
        result = login_page.login(cred_key)
        assert result == expected_result, f"Login test failed for {cred_key}"
