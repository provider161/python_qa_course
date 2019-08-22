"""
Locators for elements on header of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class Header:

    # top_links
    contacts = (By.CSS_SELECTOR, '#top-links .fa.fa-phone')
    account = (By.CSS_SELECTOR, '#top-links .fa.fa-user')
    wish_list = (By.CSS_SELECTOR, '#top-links .fa.fa-heart')
    shopping_cart = (By.CSS_SELECTOR, '#top-links .fa.fa-shopping-cart')
    checkout = (By.CSS_SELECTOR, '#top-links .fa.fa-share')

    # currencies
    currency_button = (By.CSS_SELECTOR, "#form-currency button[data-toggle='dropdown']")
    current_currency = (By.CSS_SELECTOR, "strong")
    currency_euro = (By.CSS_SELECTOR, '#form-currency [name="EUR"]')
    currency_pound = (By.CSS_SELECTOR, '#form-currency [name="GBP"]')
    currency_dollar = (By.CSS_SELECTOR, '#form-currency [name="USD"]')