import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.profile_page import ProfilePage

@allure.title("Password Recovery")
class TestForgotPassword:
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_forgot_password(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password()
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.reset_button_wait__visbl()
        element = forgot_password.reset_button()
        assert element.is_displayed()

    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_submit_recovery_email(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.submit_email()
        confirmation_message = forgot_page.fix_password_wait_visbl()
        assert confirmation_message.is_displayed()

    @allure.title("Toggle Password Visibility")
    def test_toggle_password_visibility(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_page = LoginPage(driver)
        login_page.go_to_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.submit_email()
        forgot_page.kod_from_message_wait_visbl()
        forgot_page.passord_forgot_password()
        forgot_page.toggle_password_visibility()
        element = forgot_page.password_forgon_name().get_attribute('type')
        assert element == 'text'