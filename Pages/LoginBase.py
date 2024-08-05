from Config.Config import LoginPaGeData
from Resources.Locators import LoginPageLocators
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(LoginPaGeData.BASE_URL)

    def write_username(self, username):
        self.do_send_keys(LoginPageLocators.username_input, username)

    def write_password(self,password):
        self.do_send_keys(LoginPageLocators.password_input, password)

    def click_login_button(self):
        self.do_click(LoginPageLocators.login_button)
