from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_link = page.get_by_role("link", name="Products")
        self.expected_categories = ["All Categories", "Electronics", "Sports", "Home"]
        self.products_page_url = "http://127.0.0.1:5000/products"
        self.list_group_items = page.locator(".list-group-item")
        self.category_heading = page.locator(".fw-bold")
        self.badges = page.locator(".category-badge")

    def click_products_link(self):
        self.product_link.first.click()
        expect(self.page).to_have_url(self.products_page_url)

    def get_listed_categories(self):
        """Returns the category list"""
        category_list = [name.strip() for name in self.list_group_items.all_inner_texts()]
        return category_list

    def check_all_categories_listed(self, category_list):
        """Verify all the expected categories are displayed"""
        print("Actual Categories are ", category_list)
        assert self.expected_categories == category_list, (
            f"Mismatch in categories!\nExpected: {self.expected_categories}\nFound: {category_list}"
        )

    def verify_category_badges(self, category_name):
        count = self.badges.count()
        if count == 0:
            raise AssertionError(f"No category badges found for '{category_name}'")
        for i in range(count):
            expect(self.badges.nth(i)).to_have_text(category_name)

    def each_category_products_display(self, category_list):
        """Verify user is navigated to the respective category pages"""
        for item in category_list:
            with self.page.expect_navigation():
                self.page.locator(".card-body").get_by_role("link", name=item).click()
                if item == "All Categories":
                    expect(self.category_heading).to_have_text("All Products")
                elif item in ["Electronics", "Sports", "Home"]:
                    expect(self.category_heading).to_have_text(f"{item} Products")
                    self.verify_category_badges(item)
                else:
                    raise AssertionError(f"Unexpected category encountered: {item}")
