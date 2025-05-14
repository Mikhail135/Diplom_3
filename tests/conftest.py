from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import pytest


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
