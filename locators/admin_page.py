"""
Locators for elements on admin page of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By

class AdminPage:

    logout = (By.CSS_SELECTOR, '.fa.fa-sign-out')