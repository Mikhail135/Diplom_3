from .base_page import BasePage
from locator import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ForgotPasswordPage(BasePage):
    RESET_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    def submit_email(self, email, driver):
        self.find_element(self.RESET_EMAIL_INPUT).send_keys(email)
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Data.RESET_BUTTON))
        logout_button.click()

    def toggle_password_visibility(self):
        self.find_element(self.SHOW_PASSWORD_BUTTON).click()