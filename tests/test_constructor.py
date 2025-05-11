import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locator import Locator
from pages.constructor_page import ConstructorPage
from data import Data


@allure.feature("Burger Constructor")
class TestConstructor:
    @allure.story("Всплывающее окно с деталями")
    def test_ingredient_details_popup(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        constructor_page = ConstructorPage(driver)
        constructor_page.click_of_ingredient()
        element = driver.find_element(*Locator.DETAILS_INGREDIENT)
        assert element.is_displayed()

    @allure.story("Переход на коснструктор по клику")
    def test_switch_costructor(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        profile_page.person_cab()
        profile_page.wait_web_visibility(Locator.CONSTRUCTOR_BUTTON)
        profile_page.click_of_constructor()
        element = driver.find_element(*Locator.CREAT_BURGER_TEXT)
        assert element.is_displayed()

    @allure.story("Переход на историю заказов")
    def test_history_orders(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        profile_page.click_of_lent_orders()
        profile_page.wait_web_visibility(Locator.TOTAL_ORDERS_COUNTER_TEXT)
        element = driver.find_element(*Locator.TOTAL_ORDERS_COUNTER_TEXT)
        assert element.is_displayed()

    @allure.story("Закрытие окна с ингредиентом")
    def test_close_window(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        constructor_page = ConstructorPage(driver)
        constructor_page.click_of_ingredient()
        constructor_page.wait_web_visibility(Locator.DETAILS_INGREDIENT)
        element = driver.find_element(*Locator.DETAILS_INGREDIENT)
        assert element.is_displayed()
        constructor_page.close_modale_window_num_order()
        constructor_page.wait_invis_for_all(Locator.DETAILS_INGREDIENT)
        assert True != element.is_displayed()

    @allure.story("При добавление ингрединта в заказ, каунтер увеличивается")
    def test_counter_plus(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        constructor_page = ConstructorPage(driver)
        first_counter = driver.find_element(*Locator.COUNTER_COUNT).text
        constructor_page.add_ingredient_to_order(driver)
        second_counter =driver.find_element(*Locator.COUNTER_COUNT).text
        assert second_counter > first_counter

    @allure.story("Залогиненный пользователь может оформить заказ")
    def test_order_with_auth(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login(Data.EMAIL, Data.PASSWORD)
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.wait_web_visibility(Locator.STARTED_PREPARING_ORDER)
        element = constructor_page.find_elements(Locator.STARTED_PREPARING_ORDER)
        assert element.is_displayed()


