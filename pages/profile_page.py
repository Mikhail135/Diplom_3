from .base_page import BasePage
from locator import Locator
from url import Url
import allure

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.drivers.get(Url.ACCUONT)

    @allure.step('История заказов')
    def go_to_orders_history(self):
        element = self.wait_web_clickable(Locator.ORDERS_HISTORY)
        return element

    @allure.step('Orders history script')
    def go_to_orders_history_script(self):
        orders_history = self.find_elements(Locator.ORDERS_HISTORY)
        self.execute_scripts(orders_history)

    @allure.step('Orders history wait')
    def go_to_orders_history_wait(self):
        self.wait_web_clickable(Locator.ORDERS_HISTORY)

    @allure.step('Личный кабинет')
    def person_cab(self):
        self.find_elements(Locator.PERSON_CAB).click()

    @allure.step('Личный кабинет')
    def person_cab_script(self):
        person_cab = self.find_elements(Locator.PERSON_CAB)
        self.execute_scripts(person_cab)

    @allure.step('Person cab wait')
    def person_cab_wait(self):
        self.wait_web_clickable(Locator.PERSON_CAB)

    @allure.step('Нажатие на конструктор')
    def click_of_constructor(self):
        self.find_elements(Locator.CONSTRUCTOR_BUTTON).click()

    @allure.step('Лента заказов')
    def click_of_lent_orders(self):
        self.find_elements(Locator.LENT_ORDER).click()

    @allure.step('Лента заказов')
    def click_of_lent_orders_wait(self):
        self.wait_web_clickable(Locator.LENT_ORDER)

    @allure.step('Выход из личного кабинета')
    def logout(self):
        self.wait_web_clickable(Locator.LOGOUT_BUTTON)
        self.find_elements(Locator.LOGOUT_BUTTON).click()

    @allure.step('Order history wait')
    def order_history_wait(self):
        self.wait_web_visibility(Locator.COMPLETED_ORDER_TEXT)

    @allure.step('Order history')
    def order_history(self):
        element = self.find_elements(Locator.COMPLETED_ORDER_TEXT)
        return element