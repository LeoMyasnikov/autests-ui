from playwright.sync_api import sync_playwright, expect, Page
from pages.login_page import LoginPage
import pytest

@pytest.mark.regression
@pytest.mark.autorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(email, password, login_page: LoginPage):

        # создаем экземпляр класса LoginPage
        # метод visit c base_page, который работает для всех страниц. открывает собсвенно страницу
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        # методы fill_login_form, click, check_visible_wrong_element_alert с login_page
        login_page.fill_login_form(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_element_alert()




