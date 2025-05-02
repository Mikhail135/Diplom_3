from selenium.webdriver.common.by import By


class Data:
    EMAIL = 'Mikhail_18@gmail.com'
    PASSWORD = '123456'
    ORDERS_HISTORY = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    FIX_PASSWORD = (By.XPATH, "//label[contains(text(), 'Введите код из письма')]")
    TOGGLE_ACTIVE = (By.CLASS_NAME, 'input_status_active')
    PERSON_CAB = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    CREAT_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    CLOSE_MODALE_WINDOW = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_CARD = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    DETAILS_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LENT_ORDER = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_BUTTON = (By.XPATH, "//a[contains(@class, 'OrderHistory_link__1iNby')]")
    TEXT_STRUCTURE = (By.XPATH, "//p[text()='Cостав']")
