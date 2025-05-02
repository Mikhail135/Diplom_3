from .base_page import BasePage
from selenium.webdriver.common.by import By
from locator import Data

class LentOrderPage(BasePage):
    ORDER_ITEM = (By.XPATH, "//div[contains(@class, 'order-item')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[text()='В работе']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

    def click_on_order(self):
        self.find_element(Data.ORDER_BUTTON).click()

    def get_total_orders_count(self):
        return int(self.find_element(self.TOTAL_ORDERS_COUNTER).text)

    def get_today_orders_count(self):
        return int(self.find_element(self.TODAY_ORDERS_COUNTER).text)