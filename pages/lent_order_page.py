from .base_page import BasePage
from locator import Locator
import allure

class LentOrderPage(BasePage):
    @allure.step('Нажатие на заказ')
    def click_on_order(self):
        self.find_elements(Locator.ORDER_BUTTON).click()

    @allure.step('Количество заказов')
    def get_total_orders_count(self):
        return int(self.find_elements(Locator.TOTAL_ORDERS_COUNTER).text)

    @allure.step('Количество заказов за сегодня')
    def get_today_orders_count(self):
        return int(self.find_elements(Locator.TODAY_ORDERS_COUNTER).text)