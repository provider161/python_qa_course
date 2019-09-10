"""
Class for application searchpage description.
Contains methods to interact with page parts, elements, get page information
"""

from locators.search_page import SearchPage as search_page
from locators.mainpage import MainPage as main_page


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def get_search_query_text(self):
        search_query = self.driver.find_element(*search_page.search_query)
        return search_query.text

    def get_first_result_product_name(self):
        name = self.driver.find_element(*main_page.products.product_name)
        return name.text