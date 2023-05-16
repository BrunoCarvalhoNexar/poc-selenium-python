from pom.tests.basic_test import BasicTest

class TestHome(BasicTest):


     def test_valid_home_page(self):
         self.homePage.wait_for_text_feature_items()





