import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.constructor_page import ConstructorPage
from pages.lent_order_page import LentOrderPage

@allure.title("Order Feed")
class TestFeed:
    @allure.title("Окно с деталями заказа")
    def test_order_of_lent_order(self, driver):
        profile_page = ProfilePage(driver)
        lent_order_page = LentOrderPage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.close_modal_window()
        lent_order_page.click_on_lent_order()
        constructor_page.total_orders_counter_text_wait_visbl()
        lent_order_page.click_on_order()
        element = lent_order_page.text_structure()
        assert element.is_displayed()

    @allure.title("Заказ из истории в ленте")
    def test_from_history_in_lent_order(self, driver):
        lent_order_page = LentOrderPage(driver)
        profile_page = ProfilePage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.close_modal_window()
        lent_order_page.click_on_lent_order()
        constructor_page.total_orders_counter_text_wait_visbl()
        constructor_page.total_orders_counter_wait_visbl()
        numbder_lent_order = lent_order_page.number_lent_order().text
        profile_page.person_cab_script()
        profile_page.go_to_orders_history_wait()
        profile_page.go_to_orders_history_script()
        constructor_page.completed_order_text_wait()
        numbder_from_history = lent_order_page.get_order_from_history_by_number(numbder_lent_order)
        assert numbder_from_history.text.strip('#') == numbder_lent_order.strip('#')

    @allure.title("Счётчик 'Выполнено за все время:' увеличивается")
    def test_count_up(self, driver):
        constructor_page = ConstructorPage(driver)
        profile_page = ProfilePage(driver)
        login_profile = LoginPage(driver)
        lent_order_page = LentOrderPage(driver)
        profile_page.person_cab()
        login_profile.login()
        profile_page.click_of_lent_orders()
        constructor_page.total_orders_counter_text_wait_visbl()
        numder_total_first = constructor_page.total_orders_counter().text
        print(numder_total_first)
        profile_page.click_of_constructor()
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.close_modal_window()
        lent_order_page.click_on_lent_order()
        constructor_page.total_orders_counter_text_wait_visbl()
        constructor_page.total_orders_counter_text_wait_visbl()
        numder_total_second = constructor_page.total_orders_counter().text
        print(numder_total_second)
        assert int(numder_total_first) + 1 == int(numder_total_second)


    @allure.title("Счётчик 'Выполнено за сегодня:' увеличивается")
    def test_count_up_today(self, driver):
        constructor_page = ConstructorPage(driver)
        profile_page = ProfilePage(driver)
        lent_order_page = LentOrderPage(driver)
        profile_page.person_cab()
        login_profile = LoginPage(driver)
        login_profile.login()
        profile_page.click_of_lent_orders()
        constructor_page.total_orders_counter_wait_visbl()
        numder_today_first = constructor_page.today_orders_counter().text
        profile_page.click_of_constructor()
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.close_modal_window()
        lent_order_page.click_on_lent_order()
        constructor_page.total_orders_counter_text_wait_visbl()
        constructor_page.total_orders_counter_wait_visbl()
        numder_today_second = constructor_page.today_orders_counter().text
        assert int(numder_today_first) + 1 == int(numder_today_second)

    @allure.title("номер появляется в разделе 'В работе'")
    def test_numder_in_work(self, driver):
        profile_page = ProfilePage(driver)
        login_profile = LoginPage(driver)
        lent_order_page = LentOrderPage(driver)
        constructor_page = ConstructorPage(driver)
        profile_page.person_cab()
        login_profile.login()
        constructor_page.add_ingredient_to_order(driver)
        constructor_page.craet_order()
        constructor_page.close_modal_window()
        lent_order_page.click_on_lent_order()
        constructor_page.total_orders_counter_text_wait_visbl()
        text = lent_order_page.in_work().text
        assert text != 'Все текущие заказы готовы!'





