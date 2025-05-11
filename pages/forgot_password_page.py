from .base_page import BasePage
import allure
from locator import Locator
from data import Data

class ForgotPasswordPage(BasePage):
    @allure.step('Восстановление через Email')
    def submit_email(self, email):
        self.find_elements(Locator.RESET_EMAIL_INPUT).send_keys(email)
        logout_button = self.wait_web_clickable(Locator.RESET_BUTTON)
        logout_button.click()

    @allure.step('Новый пароль')
    def passord_forgot_password(self):
        self.find_elements(Locator.PASSWORD_FORGOT_TYPE_PASSWORD).send_keys(Data.PASSWORD)

    @allure.step('Видимость пароля')
    def toggle_password_visibility(self):
        self.find_elements(Locator.SHOW_PASSWORD_BUTTON).click()
