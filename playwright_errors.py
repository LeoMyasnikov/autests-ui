from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # переменная для открытия страницы. Playwright может работать с несколькими страницами
    page = browser.new_page()
    # открываем нужную страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    unknown_element = page.locator('#unknown')
    expect(unknown_element).to_be_visible()