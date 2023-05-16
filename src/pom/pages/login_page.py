# __init__.py
from selenium.webdriver.common.by import By
from src.pom.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    link_signup_login = (By.CSS_SELECTOR,"a[href='/login']")
    field_email = (By.CSS_SELECTOR,"input[data-qa='login-email']")
    field_password = (By.CSS_SELECTOR,"input[data-qa='login-password']")
    button_login = (By.CSS_SELECTOR,"button[data-qa='login-button']")
    label_email_password_invalid = (By.XPATH,"//*[contains(text(),'Your email or password is incorrect!')]")

    def login(self,username,password):
        self.wait_for(self.link_signup_login)
        self.click(self.link_signup_login)
        self.driver.switch_to.default_content()
        self.send_keys(self.field_email, username)
        self.send_keys(self.field_password,password)
        self.click(self.button_login)

    def get_login_invalid(self):
        return self.get_text(self.label_email_password_invalid)



