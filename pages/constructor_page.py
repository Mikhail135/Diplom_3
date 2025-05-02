from .base_page import BasePage
from selenium.webdriver.common.by import By
from locator import Data
class ConstructorPage(BasePage):
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'ingredient-item')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BUN_COUNTER = (By.XPATH, "//span[text()='Булки']/following-sibling::span")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def add_ingredient_to_order(self, driver):
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.by import By
        source_element = driver.find_element(By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
        target_element = driver.find_element(By.XPATH, "//div[contains(@class, 'constructor-element')]")
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def click_of_ingredient(self):
        self.find_element(Data.INGREDIENT_CARD).click()


    def craet_order(self):
        self.find_element(Data.CREAT_ORDER).click()

    def close_modale_window_num_order(self):
        self.find_element(Data.CLOSE_MODALE_WINDOW).click()

    def get_bun_counter(self):
        return self.find_element(self.BUN_COUNTER).text

    def place_order(self):
        self.find_element(self.ORDER_BUTTON).click()
