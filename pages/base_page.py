from playwright.sync_api import Page
import allure
from typing import Literal


class BasePage:
    def __init__(self, page: Page, locale: str = 'ge-en', rel_url: str = ''):
        self._page = page
        self._base_url = 'https://www.netflix.com'
        self.locale = locale
        self.rel_url = rel_url

    @property
    def full_url(self) -> str:
        return f'{self._base_url}/{self.locale}{self.rel_url}'

    def view(self):
        with allure.step(f'Open {self.full_url}'):
            self._page.goto(self.full_url)

    def wait_for_load_state(self, state: Literal['load', 'domcontentloaded', 'networkidle'] = 'load'):
        with allure.step(f'Wait for {state} page state'):
            self._page.wait_for_load_state(state)