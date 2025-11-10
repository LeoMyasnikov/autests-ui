from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # переменная для открытия страницы. Playwright может работать с несколькими страницами
    page = browser.new_page()
    # открываем нужную страницу
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
        wait_until="networkidle")


    new_text = "New Text"
    # метод для запуска java script кода
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text }
        """,
        new_text
    )

    page.wait_for_timeout(2000)