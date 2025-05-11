import time
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locator import Locator
from selenium.webdriver.common.by import By
from pages.constructor_page import ConstructorPage
from pages.lent_order_page import LentOrderPage
from data import Data

@allure.feature("Order Feed")
class TestFeed:
    @allure.story("Окно с деталями заказа")
    def test_order_of_lent_order(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER_TEXT)
        lent_order_page = LentOrderPage(driver)
        lent_order_page.click_on_order()
        element = driver.find_element(*Locator.TEXT_STRUCTURE)
        assert element.is_displayed()

    @allure.story("Заказ из истории в ленте")
    def test_from_history_in_lent_order(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER)
        numbder_lent_order = profile_page.find_elements(Locator.NUMBDER_LENT_ORDER).text
        profile_page.person_cab()
        profile_page.go_to_orders_history(driver)
        profile_page.wait_web_visibility(Locator.COMPLETED_ORDER_TEXT)
        numbder_drom_history = driver.find_element(By.XPATH, f"//p[contains(text(), '{numbder_lent_order}')]")
        driver.execute_script("arguments[0].scrollIntoView();", numbder_drom_history)
        assert numbder_drom_history.text == numbder_lent_order

    @allure.story("Счётчик 'Выполнено за все время:' увеличивается")
    def test_count_up(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER)
        numder_today_first = profile_page.find_elements(Locator.TOTAL_ORDERS_COUNTER).text
        profile_page.click_of_constructor()
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER)
        numder_today_second = constructor_page.find_elements(Locator.TOTAL_ORDERS_COUNTER).text
        assert int(numder_today_first) + 1 == int(numder_today_second)


    @allure.story("Счётчик 'Выполнено за сегодня:' увеличивается")
    def test_count_up_today(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER)
        numder_today_first = profile_page.find_elements(Locator.TODAY_ORDERS_COUNTER).text
        profile_page.click_of_constructor()
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER)
        numder_today_second = profile_page.find_elements(Locator.TODAY_ORDERS_COUNTER).text
        assert int(numder_today_first) + 1 == int(numder_today_second)

    @allure.story("номер появляется в разделе 'В работе'")
    def test_numder_in_work(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page = ProfilePage(driver)
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER)
        text = profile_page.find_elements(Locator.IN_WORK).text
        assert text != 'Все текущие заказы готовы!'





