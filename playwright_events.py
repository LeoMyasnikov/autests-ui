# Нужно для логирования по сути

from playwright.sync_api import sync_playwright, Request, Response

# создаем 2 функции: одна печатает куда ушел request (запрос), другая - откуда пришел response и его статус (200, 500 и т.д)
def log_request(request: Request):
    print(f'Request: {request.url}')
def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')

with sync_playwright() as playwright:
    # запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # переменная для открытия страницы. Playwright может работать с несколькими страницами
    page = browser.new_page()
    # открываем нужную страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # ждем события запроса и ответа. 1- аргумент само событие, 2 - обработчик
    page.on('request', log_request)
    page.on('response', log_response)

    page.wait_for_timeout(2000)

