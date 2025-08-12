import config
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = config.LOGIN_URL
        # self.enter_username = config.USERNAME
        # self.enter_password = config.PASSWORD
        self.login_btn = page.get_by_role("img", name="Login")
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.signin_btn = page.get_by_role("button", name="Sign In")
        self.admin_dropdown = page.get_by_role("button", name="admin")

    def load_url(self):
        if not self.url:
            raise ValueError("Login URL not set in config!")
        self.page.goto(self.url)

    def login_btn_display(self):
        expect(self.login_btn).to_be_visible()

    def click_login_btn(self):
        expect(self.login_btn).to_be_enabled()
        self.login_btn.click()

    def login_page_display(self):
        expect(self.page).to_have_url(
            self.url)  # expect is recommended for Playwright as it handles waiting automatically:

    def fill_login_form(self, username, password):
        expect(self.username).to_be_visible()  # Sometimes elements take a moment to be interactable.
        self.username.fill(username)
        self.password.fill(password)

    def click_signin_btn(self):
        expect(self.signin_btn).to_be_visible()
        self.signin_btn.click()

    def login_success_display(self):
        try:
            expect(self.admin_dropdown).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            print("Admin dropdown NOT visible - login failed.")
            return False
            # raise AssertionError(
            #     "Login failed: Admin dropdown was not visible — user may not have logged in successfully.")

    def login(self, credential_type: str = "cred_key"):
        creds = getattr(config, credential_type, None)
        if not creds or "username" not in creds or "password" not in creds:
            raise ValueError(f"Invalid or missing credentials in config for: {credential_type}")

        """
        above getattr() is same as creds = config.VALID_CREDS
        But getattr() allows dynamically — it allows you to choose which variable to access based on input at runtime.
        Without getattr, you'd have to write:
        if credential_type == "VALID_CREDENTIALS":
            creds = config.VALID_CREDENTIALS
        elif credential_type == "INVALID_CREDENTIALS":
            creds = config.INVALID_CREDENTIALS
        """

        self.load_url()
        self.login_page_display()
        self.fill_login_form(creds["username"], creds["password"])
        self.click_signin_btn()
        return self.login_success_display()
