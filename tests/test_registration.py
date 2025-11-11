from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration():
    with sync_playwright() as playwright:
        # запускаем браузер
        browser = playwright.chromium.launch(headless=False)

        # используется для сохранения данных в localStorage, локаль, размер экрана и прочее
        context = browser.new_context()

        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # сохраняем состояние браузера: cookies, local storage. нужно для автоматической авторизации
        context.storage_state(path='browser-stat.json')

    with sync_playwright() as playwright:
        # запускаем браузер
        browser = playwright.chromium.launch(headless=False)

        # используем параметры авторизации из json файла авторизации
        context = browser.new_context(storage_state='browser-stat.json')
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")