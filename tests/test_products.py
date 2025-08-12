from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestProducts:
    def test_all_products_categories_listed(self, loaded_products_page):
        product_names = loaded_products_page.get_listed_categories()
        loaded_products_page.check_all_categories_listed(product_names)

    def test_verify_categories_page_listed(self, loaded_products_page):
        product_names = loaded_products_page.get_listed_categories()
        loaded_products_page.each_category_products_display(product_names)
