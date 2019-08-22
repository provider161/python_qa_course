"""
Locators for elements on admin login page of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class AdminLogin:

    username = (By.CSS_SELECTOR, "[name='username']")
    password = (By.CSS_SELECTOR, "[name='password']")
    forgotten_password = (By.CSS_SELECTOR, '.help-block a')
    login_button = (By.CSS_SELECTOR, "[type='submit']")