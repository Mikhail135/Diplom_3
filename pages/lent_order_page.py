from selenium.webdriver.common.by import By

from .base_page import BasePage
from locator import Locator
import allure


class LentOrderPage(BasePage):
    @allure.step('Нажатие на заказ')
    def click_on_order(self):
        order = self.find_elements(Locator.ORDER_BUTTON)
        self.execute_scripts(order)

    @allure.step('Lent of orders')
    def click_on_lent_order(self):
        lent = self.find_elements(Locator.LENT_ORDER)
        self.execute_scripts(lent)

    @allure.step('Количество заказов')
    def get_total_orders_count(self):
        return int(self.find_elements(Locator.TOTAL_ORDERS_COUNTER).text)

    @allure.step('Количество заказов за сегодня')
    def get_today_orders_count(self):
        return int(self.find_elements(Locator.TODAY_ORDERS_COUNTER).text)

    @allure.step('In work')
    def in_work(self):
        element = self.find_elements(Locator.IN_WORK)
        return element

    @allure.step('Number lent order')
    def number_lent_order(self):
        element = self.find_elements(Locator.NUMBDER_LENT_ORDER)
        return element

    @allure.step('Number from history')
    def get_order_from_history_by_number(self, number):
        xpath = f"//p[contains(text(), '{number}')]"
        return self.find_elements((By.XPATH, xpath))

    @allure.step('Text structure')
    def text_structure(self):
        element = self.find_elements(Locator.TEXT_STRUCTURE)
        return element
