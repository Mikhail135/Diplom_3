import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from locator import Locator
from data import Data
from pages.profile_page import ProfilePage

@allure.feature("Password Recovery")
class TestForgotPassword:
    @allure.story("Переход на страницу восстановления пароля")
    def test_navigate_to_forgot_password(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password(driver)
        element = login_page.wait_web_visibility(Locator.RESET_BUTTON)
        assert element.is_displayed()

    @allure.story("ввод почты и клик по кнопке «Восстановить»")
    def test_submit_recovery_email(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password(driver)
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.submit_email(Data.EMAIL)
        confirmation_message = forgot_page.wait_web_visibility(Locator.FIX_PASSWORD)
        assert confirmation_message.is_displayed()

    @allure.story("Toggle Password Visibility")
    def test_toggle_password_visibility(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password(driver)
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.submit_email(Data.EMAIL)
        forgot_page.wait_web_visibility(Locator.KOD_FROM_MESSAGE)
        forgot_page.passord_forgot_password()
        forgot_page.toggle_password_visibility()
        element = forgot_page.find_elements(Locator.PASSWORD_FORGOT_NAME).get_attribute('type')
        assert element == 'text'