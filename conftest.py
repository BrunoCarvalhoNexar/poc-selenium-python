import pytest
from selenium import webdriver

import settings
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(params=["firefox","chrome"])
def driver_init(request):
    global driver
    if request.param == "firefox":
        driver = webdriver.Firefox()
    if request.param == "chrome":
        driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get(settings.url)
    driver.maximize_window()
    driver.implicitly_wait(25)
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)
    yield driver
    driver.quit()


