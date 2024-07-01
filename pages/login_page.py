from playwright.sync_api import Page
from pages.base_page import BasePage
from components.login_form import LoginForm


class LoginPage(BasePage):
    def __init__(self, page: Page, locale: str = 'ge-en'):
        super().__init__(page, locale, '/login')

        self.login_form = LoginForm(page)
        self.finish_registration_button = page.locator('css=[data-uia="nmhp-card-cta+hero_fuji"]')
