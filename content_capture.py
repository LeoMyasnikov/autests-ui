from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # используется для сохранения данных в localStorage, локаль, размер экрана и прочее
    context = browser.new_context()

    page = context.new_page()
    page.goto('http://myasnikovhost/ContentCapture/Login/#/Login')

    username_input = page.locator('//input[@id="userName"]')
    username_input.fill('admin')

    password_input = page.locator('//input[@id="password"]')
    password_input.fill('password')

    auth_button = page.locator('//input[@id="loginButton"]')
    auth_button.click()

    page.wait_for_timeout(2000)

    # сохраняем состояние cookies, local storage. нужно для автоматической авторизации
    context.storage_state(path='browser-stat2.json')


with sync_playwright() as playwright:
    # запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # используем параметры авторизации из json файла авторизации
    context = browser.new_context(storage_state='browser-stat2.json')
    page = context.new_page()
    page.goto("http://myasnikovhost/ContentCapture/Login/#/PersonalPage")