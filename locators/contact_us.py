"""
Locators for elements on contact us page of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class ContactUs:

    page_topic = (By.CSS_SELECTOR, '#content h1')