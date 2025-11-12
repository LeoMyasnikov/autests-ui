# Хранятся фикстуры для работы с браузером
from playwright.sync_api import sync_playwright, Playwright
import pytest
@pytest.fixture
def chromium_main():
    with sync_playwright() as playwright:
        # Подготовка — данный код будет выполнен до начала автотеста
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page # Здесь возвращаем данные для теста


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
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

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-stat.json")
    yield context.new_page()