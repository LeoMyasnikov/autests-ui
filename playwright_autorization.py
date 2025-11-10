from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # переменная для открытия страницы. Playwright может работать с несколькими страницами
    page = browser.new_page()
    # открываем нужную страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим локатор. В переменную email_input сохраняется объект locator
    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    # указываем локатор через data_testid. playwright нативно поддерживает этот аттрибут
    email_input = page.get_by_test_id("login-form-email-input").locator('input')
    # У локатора есть метод fill.Ему мы перадаем значение и playwright это значение впишет в данный input.
    # вводим значение в поле e-mail. Через метод fill
    email_input.fill('user.name@gmail.com')

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill('Password')

    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    # указываем локатор через data_testid. playwright нативно поддерживает этот аттрибут
    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_element_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    # мы используем expect - функция, которая позволяет использовать ожидания
    # внутри передаем какой элемент нужно ожидать (какой локатор) и что мы хоти видеть. В данном случае, чтобы был виден
    expect(wrong_element_alert).to_be_visible()
    # проверяем, что найденный элемент имеет текст такой-то
    expect(wrong_element_alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(1000)
