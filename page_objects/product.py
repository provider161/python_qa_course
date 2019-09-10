"""
Class for application product page description.
Contains methods to interact with page parts, elements, get page information
"""

from locators.product import Product as product


class Product:

    def __init__(self, driver):
        self.driver = driver

    def get_price(self):
        price = self.driver.find_element(*product.product_price)
        return price.text