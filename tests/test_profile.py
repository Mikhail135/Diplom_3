import time
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locator import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.constructor_page import ConstructorPage
from data import Data
@allure.feature("Profile Functionality")
class TestProfile:
    @allure.story("История заказов")
    def test_navigate_to_orders_history(self, driver):
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
        profile_page.person_cab()
        profile_page.go_to_orders_history(driver)
        element = profile_page.find_elements(Locator.ORDER_BUTTON)
        assert element.is_displayed()

    @allure.story("Выход из профиля")
    def test_logout(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        login_profile.wait_web_visibility(Locator.CREAT_ORDER)
        profile_page.person_cab()
        profile_page.logout(driver)
        profile_page.wait_web_visibility(Locator.LOGIN_BUTTON)
        assert "login" in driver.current_url, "Logout failed"

    @allure.story("Переход в личный кабинет")
    def test_person_cab(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locator.CREAT_ORDER))
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        element = profile_page.find_elements(Locator.ORDERS_HISTORY)
        assert element.is_displayed()
