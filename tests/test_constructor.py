import time
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locator import Data
from selenium.webdriver.common.by import By
from pages.constructor_page import ConstructorPage

@allure.feature("Burger Constructor")
class TestConstructor:
    @allure.story("Всплывающее окно с деталями")
    def test_ingredient_details_popup(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        constructor_page = ConstructorPage(driver)
        constructor_page.click_of_ingredient()
        time.sleep(2)
        element = driver.find_element(*Data.DETAILS_INGREDIENT)
        assert element.is_displayed()

    @allure.story("Переход на коснструктор по клику")
    def test_switch_costructor(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        profile_page.click_of_constructor()
        element = driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']")
        assert element.is_displayed()

    @allure.story("Переход на историю заказов")
    def test_switch_costructor(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        time.sleep(2)
        profile_page.click_of_lent_orders()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//h1[text()='Лента заказов']")
        assert element.is_displayed()

    @allure.story("Закрытие окна с ингредиентом")
    def test_close_window(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        constructor_page = ConstructorPage(driver)
        constructor_page.click_of_ingredient()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//h2[text()='Детали ингредиента']")
        assert element.is_displayed()
        constructor_page.close_modale_window_num_order()
        time.sleep(2)
        assert True != element.is_displayed()

    @allure.story("При добавление ингрединта в заказ, каунтер увеличивается")
    def test_counter_plus(self, driver):
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD, driver)
        time.sleep(2)
        constructor_page = ConstructorPage(driver)
        first_counter = driver.find_element(By.XPATH, "//p[contains(@class, 'counter_counter__num__3nue1')]").text
        constructor_page.add_ingredient_to_order(driver)
        time.sleep(2)
        second_counter =driver.find_element(By.XPATH, "//p[contains(@class, 'counter_counter__num__3nue1')]").text
        assert second_counter > first_counter

    @allure.story("Залогиненный пользователь может оформить заказ")
    def test_order_with_auth(self, driver):
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


