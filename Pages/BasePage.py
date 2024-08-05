from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_amount_dropdown_elements(self,by_locator):
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        dropdown = Select(dropdown_element)
        all_options = dropdown.options
        return len(all_options)

    def select_an_option_from_dropdown(self, by_locator, option):
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(option)

