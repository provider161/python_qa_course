"""
Locators for elements on search page of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class SearchPage:

    search_query = (By.CSS_SELECTOR, '#content h1')