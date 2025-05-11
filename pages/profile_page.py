import time
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator
from url import Url
import allure

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.drivers.get(Url.ACCUONT)

    @allure.step('История заказов')
    def go_to_orders_history(self, driver):
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locator.ORDERS_HISTORY)
        )
        element.click()

    @allure.step('Личный кабинет')
    def person_cab(self):
        self.find_elements(Locator.PERSON_CAB).click()

    @allure.step('Нажатие на конструктор')
    def click_of_constructor(self):
        self.find_elements(Locator.CONSTRUCTOR_BUTTON).click()

    @allure.step('Лента заказов')
    def click_of_lent_orders(self):
        self.find_elements(Locator.LENT_ORDER).click()

    @allure.step('Выход из личного кабинета')
    def logout(self, driver):
        self.wait_web_clickable(Locator.LOGOUT_BUTTON)
        self.find_elements(Locator.LOGOUT_BUTTON).click()
