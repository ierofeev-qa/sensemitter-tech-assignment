import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page


@pytest.fixture(scope='function')
def login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    return login_page
