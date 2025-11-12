import pytest

from pages.login_page import LoginPage

# фикстура, инициирующая страницу Login_page
# в ней используем вложенную фикстуру открытия браузера и возврата страницы
@pytest.fixture
def login_page(chromium_main) -> LoginPage:
    return LoginPage(page=chromium_main)


