from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    txt_feature_items = (By.CSS_SELECTOR,"h2[class='title text-center']")

    def wait_for_text_feature_items(self):
        return self.get_text(self.txt_feature_items)




