from playwright.sync_api import Page, expect


class LandingPage:
    def __init__(self, page:Page):
        self.page = Page
        self.home_page_heading = page.locator(".display-4")

    def landing_page_display(self):
        expect(self.home_page_heading).to_have_text("Welcome to ShopEase")

