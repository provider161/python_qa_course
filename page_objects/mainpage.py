"""
Class for application homepage description.
Contains methods to interact with page parts, elements, get page information
"""

from locators.mainpage import MainPage as main_page


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def search(self, text):
        search_string = self.driver.find_element(*main_page.search_string)
        search_string.clear()
        search_string.send_keys(text)
        search_button = self.driver.find_element(*main_page.search_button)
        search_button.click()

    def switch_next_banner(self):
        next_banner_button = self.driver.find_element(*main_page.next_banner)
        next_banner_button.click()

    def check_banner_is_present(self, banner):
        if banner == 'macbook':
            self.driver.find_element(*main_page.macbook_banner)
        elif banner == 'iphone':
            self.driver.find_element(*main_page.iphone_banner)

    def open_tablets_category(self):
        tablets = self.driver.find_element(*main_page.tablets)
        tablets.click()

    def get_category_title(self):
        title = self.driver.find_element(*main_page.category_title)
        return title.text

    def get_shopping_cart_status(self):
        status = self.driver.find_element(*main_page.shopping_cart.status).text
        return status

    def open_cameras_category(self):
        cameras = self.driver.find_element(*main_page.cameras)
        cameras.click()

    def select_first_product(self):
        first_product = self.driver.find_element(*main_page.products.product_item_img)
        first_product.click()

    def select_list_view(self):
        list_view = self.driver.find_element(*main_page.products.list_view)
        list_view.click()

    def select_grid_view(self):
        grid_view = self.driver.find_element(*main_page.products.grid_view)
        grid_view.click()

    def is_grid_view(self):
        return True if self.driver.find_element(*main_page.products.grid_view) else False
