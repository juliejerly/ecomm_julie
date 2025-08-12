from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = Page
        self.products_link = page.get_by_role("link", name="Products")
        self.all_products_link = page.get_by_role("link", name="View All Products")

    def products_display(self):
        expect(self.products_link).to_be_visible()

    def all_products_display(self):
        expect(self.all_products_link).to_be_visible()
    


