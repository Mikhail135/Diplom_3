import time
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locator import Data
from selenium.webdriver.common.by import By
from pages.constructor_page import ConstructorPage
from pages.lent_order_page import LentOrderPage

@allure.feature("Order Feed")
class TestFeed:
    @allure.story("Окно с деталями заказа")
    def test_order_of_lent_order(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page = ProfilePage(driver)
        profile_page.click_of_lent_orders()
        lent_order_page = LentOrderPage(driver)
        lent_order_page.click_on_order()
        element = driver.find_element(*Data.TEXT_STRUCTURE)
        assert element.is_displayed()

    @allure.story("Заказ из истории в ленте")
    def test_from_history_in_lent_order(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        time.sleep(1)
        profile_page = ProfilePage(driver)
        profile_page.click_of_lent_orders()
        time.sleep(1)
        numbder_lent_order = driver.find_element(By.XPATH, "//p[contains(@class, 'text_type_digits-default')]").text
        profile_page.person_cab()
        profile_page.go_to_orders_history(driver)
        time.sleep(1)
        numbder_drom_history = driver.find_element(By.XPATH, f"//p[contains(text(), '{numbder_lent_order}')]")
        driver.execute_script("arguments[0].scrollIntoView();", numbder_drom_history)
        assert numbder_drom_history.text == numbder_lent_order

    @allure.story("Счётчик 'Выполнено за все время:' увеличивается")
    def test_count_up(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        profile_page = ProfilePage(driver)
        profile_page.click_of_lent_orders()
        time.sleep(1)
        numder_today_first = driver.find_element(By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]").text
        profile_page.click_of_constructor()
        time.sleep(3)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        time.sleep(1)
        profile_page.click_of_lent_orders()
        time.sleep(1)
        numder_today_second = driver.find_element(By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]").text
        assert int(numder_today_first) + 1 == int(numder_today_second)


    @allure.story("Счётчик 'Выполнено за сегодня:' увеличивается")
    def test_count_up_today(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        profile_page = ProfilePage(driver)
        profile_page.click_of_lent_orders()
        time.sleep(1)
        numder_today_first = driver.find_element(By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]").text
        profile_page.click_of_constructor()
        time.sleep(3)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        time.sleep(1)
        profile_page.click_of_lent_orders()
        time.sleep(1)
        numder_today_second = driver.find_element(By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]").text
        assert int(numder_today_first) + 1 == int(numder_today_second)

    @allure.story("номер появляется в разделе 'В работе'")
    def test_numder_in_work(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(3)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page = ProfilePage(driver)
        profile_page.click_of_lent_orders()
        time.sleep(4)
        text = driver.find_element(By.XPATH, "//li[contains(@class, 'text')]").text
        assert text != 'Все текущие заказы готовы!'





