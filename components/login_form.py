from playwright.sync_api import Page


class LoginForm:
    def __init__(self, page: Page):
        self.locator_login_input = page.locator('css=[data-uia="login-field"]')
        self.locator_password_input = page.locator('css=[data-uia="password-field"]')
        self.locator_submit_button = page.locator('css=[data-uia="login-submit-button"]')
