from playwright.sync_api import sync_playwright, Playwright
import pytest
@pytest.fixture
def chromium_main():
    with sync_playwright() as playwright:
        # Подготовка — данный код будет выполнен до начала автотеста
        browser = playwright.chromium.launch(headless=False)
        yield browser # Здесь возвращаем данные для теста


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

# Можем использовать фикстуру playwright, убрав with sync_playwright() as playwright:
# Пример:
@pytest.fixture
def chromium_main2(playwright: Playwright):
        # Подготовка — данный код будет выполнен до начала автотеста
        browser = playwright.chromium.launch(headless=False)
        yield browser # Здесь возвращаем данные для теста
