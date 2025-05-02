import time
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Data


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://stellarburgers.nomoreparties.site/account")

    def go_to_orders_history(self, driver):
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Data.ORDERS_HISTORY)
        )
        element.click()

    def person_cab(self):
        time.sleep(2)
        self.find_element(Data.PERSON_CAB).click()

    def click_of_constructor(self):
        self.find_element(Data.CONSTRUCTOR_BUTTON).click()

    def click_of_lent_orders(self):
        time.sleep(1)
        self.find_element(Data.LENT_ORDER).click()

    def logout(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Data.LOGOUT_BUTTON))
        self.find_element(Data.LOGOUT_BUTTON).click()
