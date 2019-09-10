"""
Class for application searchpage description.
Contains methods to interact with page parts, elements, get page information
"""

from locators.search_page import SearchPage as search_page


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def get_search_query_text(self):
        search_query = self.driver.find_element(*search_page.search_query)
        return search_query.text
