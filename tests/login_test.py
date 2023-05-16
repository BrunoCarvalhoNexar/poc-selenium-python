import settings
from tests.basic_test import BasicTest

class TestLogin(BasicTest):


     def test_login(self):
         self.loginPage.login(settings.username,settings.password)

     def test_login_invalid(self):
         self.loginPage.login(settings.username,settings.password_wrong)
         assert self.loginPage.get_login_invalid() == "Your email or password is incorrect!"