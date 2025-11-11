from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture
def chromium_main():
    with sync_playwright() as playwright:
        # Подготовка — данный код будет выполнен до начала автотеста
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page # Здесь возвращаем данные для теста
        # Очистка — данный код будет выполнен после завершения автотеста
        print("Teardown: закрываем браузер")
        browser.close()  # Закрываем окно браузера (teardown)


# pytest позволяет создавать несколько файлов conftest.py в разных каталогах. Фикстуры в них будут применяться только к тестам в том же каталоге и подкаталогах. Это удобно для разделения контекста и создания фикстур, специфичных для определенных частей проекта.
#
# Пример организации файлов:
#
# .
# └── tests/
#     ├── conftest.py # Фикстуры будут доступны во всех автотестах
#     ├── registration/
#     │   ├── conftest.py # Фикстуры будут доступны ТОЛЬКО в рамках модуля registration
#     │   ├── test_registration.py
#     │   └── test_admin_registration.py
#     └── authorization/
#         ├── conftest.py # Фикстуры будут доступны ТОЛЬКО в рамках модуля authorization
#         ├── test_authorization.py
#         └── test_admin_authorization.py
#
#
# Глобальный conftest.py: фикстуры в tests/conftest.py будут доступны во всех тестах.
# Локальные conftest.py: фикстуры в registration/conftest.py будут доступны только в registration.