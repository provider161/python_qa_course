"""
Locators for elements on footer of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class Footer:

    about_us = (By.XPATH, '//*[text() = "About Us"]')
    delivery_information = (By.XPATH, '//*[text() = "Delivery Information"]')
    privacy_policy = (By.XPATH, '//*[text() = "Privacy Policy"]')
    terms_conditions = (By.XPATH, '//*[text() = "Terms & Conditions"]')
    contact_us = (By.XPATH, '//*[text() = "Contact Us"]')
    returns = (By.XPATH, '//*[text() = "Returns"]')
    site_map = (By.XPATH, '//*[text() = "Site Map"]')
    brands = (By.XPATH, '//*[text() = "Brands"]')
    gift_certificates = (By.XPATH, '//*[text() = "Gift Certificates"]')
    affiliate = (By.XPATH, '//*[text() = "Affiliate"]')
    specials = (By.XPATH, '//*[text() = "Specials"]')
    my_account = (By.XPATH, '//*[text() = "My Account"]')
    order_history = (By.XPATH, '//*[text() = "Order History"]')
    wish_list = (By.XPATH, '//*[text() = "Wish List"]')
    newsletter = (By.XPATH, '//*[text() = "Newsletter"]')