from behave import *
from selenium import webdriver
from Config.Config import LoginPaGeData
from Pages.LoginBase import LoginPage
from Pages.HomePage import HomePage
import unittest

@given(u'A Login website')
def given_a_url(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.driver.get(LoginPaGeData.BASE_URL)


@when(u'The username and password are input')
def step_username_and_password_enter(context):
    context.login_page.write_username(LoginPaGeData.USERNAME)
    context.login_page.write_password(LoginPaGeData.PASSWORD)

@when(u'I click in the login button')
def step_click_login_button(context):
    context.login_page.click_login_button()

@then(u'The login is successful')
def step_then_see_home_page(context):
    context.home_page = HomePage(context.driver)
    assert "Products" in context.home_page.wait_for_home_page()

