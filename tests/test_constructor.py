import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.constructor_page import ConstructorPage


@allure.title("Burger Constructor")
class TestConstructor:
    @allure.title("Всплывающее окно с деталями")
    def test_ingredient_details_popup(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page = ConstructorPage(driver)
        constructor_page.click_of_ingredient()
        element = constructor_page.detaikss_ingredient()
        assert element.is_displayed()

    @allure.title("Переход на коснструктор по клику")
    def test_switch_costructor(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        profile_page.person_cab()
        constructor_page = ConstructorPage(driver)
        constructor_page.constructor_button()
        profile_page.click_of_constructor()
        element = constructor_page.creat_burger_text()
        assert element.is_displayed()

    @allure.title("Переход на историю заказов")
    def test_history_orders(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        profile_page.go_to_orders_history().click()
        profile_page.order_history_wait()
        element = profile_page.order_history()
        assert element.is_displayed()

    @allure.title("Закрытие окна с ингредиентом")
    def test_close_window(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page = ConstructorPage(driver)
        constructor_page.click_of_ingredient()
        constructor_page.details_ingredient_wait_visbl()
        element = constructor_page.detaikss_ingredient()
        assert element.is_displayed()
        constructor_page.close_modale_window_num_order()
        constructor_page.details_ingredient_wait_invis_for_all()
        assert True != element.is_displayed()

    @allure.title("При добавление ингрединта в заказ, каунтер увеличивается")
    def test_counter_plus(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page = ConstructorPage(driver)
        first_counter = constructor_page.counter_count().text
        constructor_page.add_ingredient_to_order(driver)
        second_counter = constructor_page.counter_count().text
        assert second_counter > first_counter

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_order_with_auth(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.started_preparing_order_wait()
        element = constructor_page.started_preparing_order()
        assert element.is_displayed()


