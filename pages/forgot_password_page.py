from .base_page import BasePage
import allure
from locator import Locator
from data import Data

class ForgotPasswordPage(BasePage):
    @allure.step('Восстановление через Email')
    def submit_email(self):
        self.find_elements(Locator.RESET_EMAIL_INPUT).send_keys(Data.EMAIL)
        logout_button = self.wait_web_clickable(Locator.RESET_BUTTON)
        logout_button.click()

    @allure.step('Новый пароль')
    def passord_forgot_password(self):
        self.find_elements(Locator.PASSWORD_FORGOT_TYPE_PASSWORD).send_keys(Data.PASSWORD)

    @allure.step('Видимость пароля')
    def toggle_password_visibility(self):
        self.find_elements(Locator.SHOW_PASSWORD_BUTTON).click()

    @allure.step('Reset button wait visbl')
    def reset_button_wait__visbl(self):
        self.wait_web_visibility(Locator.RESET_BUTTON)

    @allure.step('Reset button')
    def reset_button(self):
        element = self.find_elements(Locator.RESET_BUTTON)
        return element
    @allure.step('Fix password')
    def fix_password_wait_visbl(self):
        element = self.wait_web_visibility(Locator.FIX_PASSWORD)
        return element

    @allure.step('Password forgot name')
    def password_forgon_name(self):
        element = self.find_elements(Locator.PASSWORD_FORGOT_NAME)
        return element


    @allure.step('Kod from message')
    def kod_from_message_wait_visbl(self):
        self.wait_web_visibility(Locator.KOD_FROM_MESSAGE)