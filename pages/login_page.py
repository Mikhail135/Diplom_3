from data import Data
from .base_page import BasePage
from locator import Locator
import allure

class LoginPage(BasePage):
    @allure.step('Вход в личный кабинет')
    def login(self):
        self.wait_invis()
        self.find_elements(Locator.EMAIL_INPUT).send_keys(Data.EMAIL)
        self.find_elements(Locator.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        self.find_elements(Locator.LOGIN_BUTTON).click()
        self.wait_web_visibility(Locator.CREAT_ORDER)

    @allure.step('Восстановление пароля')
    def go_to_forgot_password(self):
        forgot_password_link = self.find_elements(Locator.FORGOT_PASSWORD_LINK)
        forgot_password_link.click()

    @allure.step('Login button wait')
    def login_button_wait(self):
        self.wait_web_visibility(Locator.LOGIN_BUTTON)
