import pytest

# передаем параметры в тест через деоратор mark.parametrize. Если несколько параметров, то записывается через запятую

@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(email, password, chromium_main):
    page = chromium_main.new_page()
    # открываем нужную страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим локатор. В переменную email_input сохраняется объект locator
    email_input = page.get_by_test_id("login-form-email-input").locator('input')
    email_input.fill(email)

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill(password)

    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()


# Иногда нужно передать не только значения, но и дополнительную информацию,
# например, отметить, что тест должен быть пропущен или ожидать конкретного исключения.
# В этом примере третий тест будет пропущен, так как он помечен pytest.mark.skip:
@pytest.mark.parametrize("value", [
    pytest.param(1),
    pytest.param(2),
    pytest.param(-1, marks=pytest.mark.skip(reason="Negative value")),
])
def test_increment(value):
    assert value > 0


# Пример перемножения параметров. Например, нужно запустить тест на комбинации версии os и браузера
@pytest.mark.parametrize('os', ['macos', 'windows', 'linux'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    run_test = browser, os
    assert run_test


# Параметризовать можно не только тестовые функции, но и фикстуры.
# Это полезно, когда нужно передать разные параметры в фикстуру, а затем использовать их в разных тестах.
# Передаем системный аргумент request в функцию. В этом аргументе передается параметр фиксутры
# Здесь фикстура browser будет передавать различные значения браузеров, и тест test_browser выполнится три раза — по одному на каждый браузер:
@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request):
    return request.param

def test_browser(browser):
    assert browser in ["chrome", "firefox", "safari"]


# Иногда удобнее передавать значения в виде словарей, особенно если параметры могут изменяться:
@pytest.mark.parametrize("data", [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "admin", "password": "admin123"},
])
def test_login(data):
    assert login(data["username"], data["password"]) == "Success"


# параметризация тестового класса
@pytest.mark.parametrize('user', ['Lev', 'Anna'])
class TestOperations:
    def test_user_without_operations(self, user):
        ...

    def test_user_with_operations(self, user):
        ...


# ids - добавляет описание параметра. Можно так же указать ids = None
@pytest.mark.parametrize(
    'phone_number',
    ['+798123243', '+34357634'],
    ids=[
        'User1',
        'User2'
    ]
)
def test_identifiers(phone_number):
    ...

