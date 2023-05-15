from tests.basic_test import BasicTest

class TestLogin(BasicTest):


     def test_login(self):
         self.loginPage.login()