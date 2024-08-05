from Pages.BasePage import BasePage
from Resources.Locators import HomePageLocators as HL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def wait_for_home_page(self):
        product = self.get_element_text(HL.product_label)
        return product
