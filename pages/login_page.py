from playwright.sync_api import sync_playwright, expect
import pytest
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page) # инициализируем page класса BasePage

        # обозначаем локаторы в виде аттрибутов класса
        self.email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        self.password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        self.login_button = page.locator('//button[@data-testid="login-page-login-button"]')
        self.registration_link = page.locator('//a[@data-testid="login-page-registration-link"]')
        self.wrong_element_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')

    def fill_login_form(self, email, password):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_visible_wrong_element_alert(self):
        # внутри передаем какой элемент нужно ожидать (какой локатор) и что мы хоти видеть. В данном случае, чтобы был виден
        expect(self.wrong_element_alert).to_be_visible()
        # проверяем, что найденный элемент имеет текст такой-то
        expect(self.wrong_element_alert).to_have_text('Wrong email or password')




