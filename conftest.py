# conftest.py

import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture(scope="session")
def logged_in_context():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    login_page = LoginPage(context.new_page())
    login_page.login("VALID_CREDS")
    yield context  # Reuse this context in all tests
    browser.close()
    p.stop()


@pytest.fixture(scope="session")
def page(logged_in_context):
    # Fresh page from logged-in context for each test
    page = logged_in_context.pages[0]
    yield page
    page.close()


@pytest.fixture
def loaded_products_page(page):
    products_page = ProductsPage(page)
    products_page.click_products_link()
    return products_page
