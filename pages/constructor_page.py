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

    @allure.step('Закрытие модального окна')
    def close_modale_window_num_order(self):
        close_window = self.wait_web_clickable(Locator.CLOSE_MODALE_WINDOW)
        close_window.click()

    @allure.step('Количество булок')
    def get_bun_counter(self):
        return self.find_elements(Locator.BUN_COUNTER).text

    @allure.step('Заказ')
    def place_order(self):
        self.find_elements(Locator.ORDER_BUTTON).click()
