from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    link_signup_login = (By.CSS_SELECTOR,"a[href='/login']")

    def login(self):
        self.click(self.link_signup_login)