from playwright.sync_api import Page


class LoginForm:
    def __init__(self, page: Page):
        self.locator_login_input = page.locator('css=[data-uia="login-field"]')
        self.locator_password_input = page.locator('css=[data-uia="password-field"]')
        self.locator_submit_button = page.locator('css=[data-uia="login-submit-button"]')

    def login(self, login: str, password: str) -> None:
        self.locator_login_input.fill(login)
        self.locator_password_input.fill(password)
        self.locator_submit_button.click()
