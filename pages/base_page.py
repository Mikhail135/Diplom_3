from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import Url
from tests.conftest import driver
from locator import Locator


class BasePage:
    def __init__(self, driver):
        self.drivers = driver
        self.wait = WebDriverWait(driver, 10)

    def find_elements(self, locator):
        return self.drivers.find_element(*locator)

    def wait_web_lacoted(self, locator):
        element = WebDriverWait(self.drivers, 10).until(
            EC.invisibility_of_element_located(locator))
        return element

    def wait_web_clickable(self, locator):
        element = WebDriverWait(self.drivers, 20).until(
            EC.element_to_be_clickable(locator))
        return element

    def wait_web_visibility(self, locator):
        element = WebDriverWait(self.drivers, 10).until(
            EC.visibility_of_element_located(locator))
        return element

    def wait_invis(self):
        WebDriverWait(self.drivers, 10).until(
            EC.invisibility_of_element(Locator.MODAL_OVERLAY))

    def wait_invis_for_all(self, locator):
        WebDriverWait(self.drivers, 10).until(
            EC.invisibility_of_element_located(locator))

    def get_forgot_link(self):
        self.drivers.get(Url.FORGOT_PASSWORD)

    def click_virt_mouse(self, locator):
        action = ActionChains(self.drivers)
        WebDriverWait(self.drivers, 5).until(EC.element_to_be_clickable(locator))
        element = self.drivers.find_element(*locator)
        action.click(on_element=element).perform()

    def click_element_via_js(self, locator):
        element = self.drivers.find_element(*locator)
        self.drivers.execute_script("arguments[0].click();", element)

    def implicitly_wait(self):
        self.drivers.implicitly_wait(10)



