import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "safari"])
def driver_init(request):
    global driver
    if request.param == "chrome":
       driver = webdriver.Chrome()
    if request.param == "safari":
       driver = webdriver.Safari()
    request.cls.driver = driver
    driver.get("https://automationexercise.com/")
    driver.implicitly_wait(20)
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)
    yield driver
    driver.quit()


