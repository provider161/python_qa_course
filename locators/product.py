"""
Locators for elements on product page of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class Product:

    add_to_wish_list = (By.CSS_SELECTOR, 'button[data-original-title="Add to Wish List"]')
    compare_product = (By.CSS_SELECTOR, 'button[data-original-title="Compare this Product"]')
    product_name = (By.CSS_SELECTOR, '#content h1')
    product_price = (By.XPATH, "//li[contains(text(), 'Ex Tax')]/parent::ul//h2")
    quantity = (By.CSS_SELECTOR, '#input-quantity')
    add_to_cart = (By.CSS_SELECTOR, '#button-cart')
    description = (By.XPATH, '//*[text() = "Description"]')
    specification = (By.XPATH, '//*[text() = "Specification"]')
    reviews = (By.XPATH, '//*[contains(text(), "Reviews")]')
