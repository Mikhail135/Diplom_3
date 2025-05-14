import allure
from .base_page import BasePage
from url import Url
from locator import Locator
from selenium.webdriver.common.action_chains import ActionChains

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.drivers.get(Url.FRONT_SITE)

    @allure.step('Добавление ингредиента')
    def add_ingredient_to_order(self, driver):
        source_element = driver.find_element(*Locator.INGREDIENT_CARD_SWAP)
        target_element = driver.find_element(*Locator.INGREDIENT_CARD_SWAP_GOAL)
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step('Нажатие на ингредиент')
    def click_of_ingredient(self):
        self.find_elements(Locator.INGREDIENT_CARD).click()

    @allure.step('Создание заказа')
    def craet_order(self):
        self.find_elements(Locator.CREAT_ORDER).click()

    @allure.step('Creat order wait')
    def craet_order_wait_visbl(self):
        self.wait_web_visibility(Locator.CREAT_ORDER)

    @allure.step('Закрытие модального окна')
    def close_modale_window_num_order_wait(self):
        self.wait_web_clickable(Locator.CLOSE_MODALE_WINDOW)


    @allure.step('Закрытие модального окна')
    def close_modale_window_num_order(self):
        close_window = self.find_elements(Locator.CLOSE_MODALE_WINDOW)
        close_window.click()


    @allure.step('Количество булок')
    def get_bun_counter(self):
        return self.find_elements(Locator.BUN_COUNTER).text

    @allure.step('Заказ')
    def place_order(self):
        element = self.find_elements(Locator.ORDER_BUTTON)
        return element

    @allure.step('Order wait')
    def place_order_wait(self):
        self.wait_web_visibility(Locator.ORDER_BUTTON)

    @allure.step('Detals ingredient')
    def detaikss_ingredient(self):
        element = self.find_elements(Locator.DETAILS_INGREDIENT)
        return element

    @allure.step('Details ingredient')
    def details_ingredient_wait_visbl(self):
        element = self.wait_web_visibility(Locator.DETAILS_INGREDIENT)
        return element

    @allure.step('Details ingrefient for all')
    def details_ingredient_wait_invis_for_all(self):
        element = self.wait_invis_for_all(Locator.DETAILS_INGREDIENT)
        return element

    @allure.step('Close modale window')
    def close_modal_window(self):
        modal = self.find_elements(Locator.CLOSE_MODALE_WINDOW)
        self.execute_scripts(modal)

    @allure.step('Constructor button')
    def constructor_button(self):
        element = self.wait_web_visibility(Locator.CONSTRUCTOR_BUTTON)
        return element

    @allure.step('Creat Burger Text')
    def creat_burger_text(self):
        element = self.find_elements(Locator.CREAT_BURGER_TEXT)
        return element

    @allure.step('Total order counter text')
    def total_orders_counter_text(self):
        element = self.find_elements(Locator.TOTAL_ORDERS_COUNTER_TEXT)
        return element

    @allure.step('Total order counter')
    def total_orders_counter(self):
        element = self.find_elements(Locator.TOTAL_ORDERS_COUNTER)
        return element

    @allure.step('Total order counter wait')
    def total_orders_counter_wait_visbl(self):
        self.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER)

    @allure.step('Total order counter wait text')
    def total_orders_counter_text_wait_visbl(self):
        self.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER_TEXT)

    @allure.step('Total order counter wait')
    def today_orders_counter(self):
        element = self.find_elements(Locator.TODAY_ORDERS_COUNTER)
        return element

    @allure.step('Counter count')
    def counter_count(self):
        element = self.find_elements(Locator.COUNTER_COUNT)
        return element

    @allure.step('Started preparing order wait')
    def started_preparing_order_wait(self):
        self.wait_web_visibility(Locator.STARTED_PREPARING_ORDER)

    @allure.step('Started preparing order')
    def started_preparing_order(self):
        element = self.find_elements(Locator.STARTED_PREPARING_ORDER)
        return element

    @allure.step('Completed order text wait')
    def completed_order_text_wait(self):
        self.wait_web_visibility(Locator.COMPLETED_ORDER_TEXT)

