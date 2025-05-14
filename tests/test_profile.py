import time
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.constructor_page import ConstructorPage

@allure.title("Profile Functionality")
class TestProfile:
    @allure.title("История заказов")
    def test_navigate_to_orders_history(self, driver):
        profile_page = ProfilePage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.close_modal_window()
        profile_page.person_cab_script()
        profile_page.go_to_orders_history_wait()
        profile_page.go_to_orders_history_script()
        constructor_page.place_order_wait()
        element = constructor_page.place_order()
        assert element.is_displayed()

    @allure.title("Выход из профиля")
    def test_logout(self, driver):
        profile_page = ProfilePage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page.craet_order_wait_visbl()
        profile_page.person_cab()
        profile_page.logout()
        login_profile.login_button_wait()
        assert "login" in driver.current_url, "Logout failed"

    @allure.title("Переход в личный кабинет")
    def test_person_cab(self, driver):
        profile_page = ProfilePage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page.craet_order_wait_visbl()
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        element = profile_page.go_to_orders_history()
        assert element.is_displayed()
