from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_input = (By.ID, "user-name")
    password_input = (By.XPATH, "//input[@data-test='password']")
    login_button = (By.ID, "login-button")

class HomePageLocators:
    product_label = (By.XPATH, "//*[@id='inventory_filter_container']/div")

