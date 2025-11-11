from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(autouse=True) # данная фикстура будет автоматически запускаться, даже без добавления в тест
def send_analitycs_data():
    print("[Autouse] Отправляем данные в сервис аналитики")
    ...

# Фикстуры можно применять на разных уровнях:
#
# scope="function" (по умолчанию): выполняется перед каждым тестом. Запускаться один раз на функцию
# Обычно используется для таких действий, как открытие браузера, создание какой-либо сущности, создание/удаление данных до/после автотеста. Самый часто используемый scope
# scope="module": выполняется один раз на уровне модуля. Определение module в python. Очень редко используется
# scope="class": выполняется один раз для каждого класса с тестами. Используется для таких действий, как создание данных, которые нужны для всего тестового класса
# scope="session": выполняется один раз за всю сессию тестирования. Используется для данных, которые нужны для всей тестовой сессии, например настройки автотестов

@pytest.fixture(scope="function") # используется по дефолту. Например, открываем браузер на каждый автотест
def function_browser():
    print("Данная фикстура будет запущена на каждый автотест")

@pytest.fixture(scope="class") #Здесь создаем данные пользователя один раз на тестовый класс
def class_browser():
    print("Данная фикстура будет запущена на каждый тестовый класс")

@pytest.fixture(scope="session") #Здесь например инициализируем настройки автотестов
def session_browser():
    print("Данная фикстура будет запущена один раз на всю тестовую сессию")

@pytest.fixture(scope="module")
def module_browser():
    print("Данная фикстура будет запущена на каждый модуль python")


class TestUserFlow:
    def test_user_can_login(self, session_browser, class_browser, function_browser):
        ...

    def test_user_can_create_license(self, session_browser, class_browser, function_browser):
        ...


class TestAccountFlow:
    def test_user_account(self, session_browser, class_browser, function_browser):
        ...

# Фикстуры часто используются для подготовки данных для тестов. Например, фикстура может вернуть тестовые данные, которые используются в нескольких тестах.
# Пример:


@pytest.fixture
def user_data():
    return {"username": "test_user", "email": "test@example.com"}

def test_user_email(user_data):
    assert user_data["email"] == "test@example.com"

def test_user_username(user_data):
    assert user_data["username"] == "test_user"


# Фикстуры также могут использоваться для инициализации ресурсов, таких как соединение с базой данных, открытие файлов, открытие браузера и т.д.
# Пример:


@pytest.fixture
def chromium():
    with sync_playwright() as playwright:
        # Подготовка — данный код будет выполнен до начала автотеста
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page # Здесь возвращаем данные для теста
        # Очистка — данный код будет выполнен после завершения автотеста
        print("Teardown: освобождение ресурса")
        browser.close()  # Закрываем окно браузера (teardown)


class TestOpenPage:
    def test_user_can_login(self, chromium): # Внутри автотеста уже работает с готовым объектом браузера
        chromium.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        chromium.wait_for_timeout(1000)


# Фикстуры могут выполнять не только setup (подготовку ресурсов), но и teardown (очистку ресурсов) с помощью ключевого слова yield.
# Все, что идет после yield, выполняется после завершения теста.
#
# Разбор Setup и Teardown в контексте фикстур в pytest
# Setup и Teardown — это два важных этапа в процессе тестирования, которые отвечают за подготовку и завершение работы каждого теста.
# Setup — это код, который выполняется перед тестом. Он нужен для подготовки необходимых ресурсов, таких как создание тестовых данных, настройка окружения, подключение к базе данных и т.д.
# Teardown — это код, который выполняется после теста. Его задача — очистить за собой всё, что было создано в процессе теста, например, закрыть соединения с базами данных, удалить временные файлы или вернуть состояние системы в исходное.
# В pytest это реализуется через фикстуры, которые обеспечивают настройку и очистку состояния тестов.
# Вместо того чтобы повторять код setup и teardown в каждом тесте, фикстуры позволяют инкапсулировать эту логику и использовать её повторно в разных тестах.
# Пример:

@pytest.fixture
def setup_teardown():
    # Это часть Setup — код, который выполняется перед тестом
    print("Setup: Инициализация данных или окружения")
    test_data = {"user": "testuser", "password": "testpass"}

    # Это часть Teardown — код, который выполняется после теста
    yield test_data  # Здесь возвращаем данные для теста

    print("Teardown: Очистка данных или окружения")
    # Здесь можно закрыть соединения, удалить временные файлы и т.д.
    # Например, удалить созданные записи в базе данных, если таковые были.


def test_login(setup_teardown):
    # Здесь setup_teardown будет содержать возвращённые данные из фикстуры
    assert setup_teardown["user"] == "testuser"
    assert setup_teardown["password"] == "testpass"


# Фикстуры могут зависеть от других фикстур, что упрощает создание сложных цепочек зависимостей между ресурсами.
# Пример:

@pytest.fixture
def playwright(): # Инициализируем фикстуру playwright
    return

@pytest.fixture
def chromium(playwright): # Передаем фикстуру playwright
    return playwright.chromium.launch()

def test_user_can_login(chromium):
    chromium.goto("http://localhost:7000/login")
