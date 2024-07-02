import os
import pytest
from playwright.sync_api import expect
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.parametrize('test_locale, expected_text', [
    ('us-en', 'Finish Sign Up'),
    ('ge-ru', 'Завершить оформление подписки')
])
def test_login(login_page, test_locale, expected_text):
    login_page.locale = test_locale
    login_page.view()
    login_page.wait_for_load_state('networkidle')

    login_page.login_form.login(os.getenv('TEST_EMAIL'), os.getenv('TEST_PASSWORD'))

    expect(login_page.finish_registration_button).to_be_visible()
    expect(login_page.finish_registration_button).to_have_text(expected_text)
