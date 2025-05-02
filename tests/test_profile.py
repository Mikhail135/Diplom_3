import time
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locator import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.constructor_page import ConstructorPage
@allure.feature("Profile Functionality")
class TestProfile:
    @allure.story("История заказов")
    def test_navigate_to_orders_history(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        time.sleep(5)
        constructor_page.close_modale_window_num_order()
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        profile_page.go_to_orders_history(driver)
        time.sleep(1)
        element = driver.find_element(By.XPATH, "//a[contains(@class, 'OrderHistory_link__1iNby')]")
        assert element.is_displayed()


    @allure.story("Выход из профиля")
    def test_logout(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Data.CREAT_ORDER))
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        profile_page.logout(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Data.LOGIN_BUTTON))
        assert "login" in driver.current_url, "Logout failed"




    @allure.story("Переход в личный кабинет")
    def test_person_cab(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Data.CREAT_ORDER))
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        element = driver.find_element(By.XPATH, "//a[text()='История заказов']")

        assert element.is_displayed()
