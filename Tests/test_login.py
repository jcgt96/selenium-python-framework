from Config.Config import LoginPaGeData
from Tests.test_base import BaseTest
from Pages.LoginBase import LoginPage


class TestLogin(BaseTest):

    def test_login(self):
        self.login_test = LoginPage(self.driver)
        self.login_test.sample_login(LoginPaGeData.USERNAME, LoginPaGeData.PASSWORD)
