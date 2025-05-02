import time
from tests.conftest import driver
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locator import Data

class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    def login(self, email, password, driver):
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")),
            "Modal overlay is still visible"
        )
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        time.sleep(2)
        self.find_element(Data.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Data.CREAT_ORDER))

    def go_to_forgot_password(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")),
                "Modal overlay is still visible"
            )
            self.scroll_to_element(self.FORGOT_PASSWORD_LINK)
            forgot_password_link = self.find_element(self.FORGOT_PASSWORD_LINK)
            forgot_password_link.click()
        except Exception as e:
                # Если всё ещё не получается кликнуть, используем JavaScript
            forgot_password_link = self.find_element(self.FORGOT_PASSWORD_LINK)
            self.driver.execute_script("arguments[0].click();", forgot_password_link)