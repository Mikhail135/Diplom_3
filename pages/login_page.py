from tests.conftest import driver
from .base_page import BasePage
from locator import Locator
import allure
from pages.forgot_password_page import ForgotPasswordPage

class LoginPage(BasePage):
    @allure.step('Вход в личный кабинет')
    def login(self, email, password):
        self.wait_invis()
        self.find_elements(Locator.EMAIL_INPUT).send_keys(email)
        self.find_elements(Locator.PASSWORD_INPUT).send_keys(password)
        self.find_elements(Locator.LOGIN_BUTTON).click()
        self.wait_web_visibility(Locator.CREAT_ORDER)

    @allure.step('Восстановление пароля')
    def go_to_forgot_password(self, driver):
        try:
            forgot_password = ForgotPasswordPage(driver)
            forgot_password_link = forgot_password.find_elements(Locator.FORGOT_PASSWORD_LINK)
            forgot_password_link.click()
        except Exception as e:
            forgot_password_link = self.find_elements(Locator.FORGOT_PASSWORD_LINK)
            self.execute_script("arguments[0].click();", forgot_password_link)