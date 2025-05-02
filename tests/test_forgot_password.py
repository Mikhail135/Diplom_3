import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Data


@allure.feature("Password Recovery")
class TestForgotPassword:
    @allure.story("Переход на страницу восстановления пароля")
    def test_navigate_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password()
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Data.RESET_BUTTON)
        )
        assert element.is_displayed()

    @allure.story("ввод почты и клик по кнопке «Восстановить»")
    def test_submit_recovery_email(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.submit_email(Data.EMAIL, driver)
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Data.FIX_PASSWORD)
        )
        assert confirmation_message.is_displayed(), "Confirmation message is not displayed"

    @allure.story("Toggle Password Visibility")
    def test_toggle_password_visibility(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.submit_email(Data.EMAIL, driver)
        forgot_page.toggle_password_visibility()
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Data.TOGGLE_ACTIVE)
        )
        assert element.is_displayed()