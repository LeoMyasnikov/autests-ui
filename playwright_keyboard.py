from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # переменная для открытия страницы. Playwright может работать с несколькими страницами
    page = browser.new_page()
    # открываем нужную страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')

    # вводим в поле текст с клавиатуры. Можно глянуть в документации: https://playwright.dev/python/docs/api/class-keyboard
    email_input.focus()
    # для каждой буквы в этом тексте мы печатаем соответствующую букву
    for char in 'user.name@gmail.com':
        page.keyboard.type(char)

    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(1000)