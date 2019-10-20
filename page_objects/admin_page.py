"""
Class for admin page
"""

from locators.admin_page import AdminPage as admin_page


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        button = self.driver.find_element(*admin_page.logout)
        button.click()

    def open_downloads(self):
        catalog = self.driver.find_element(*admin_page.navigation.catalog)
        catalog.click()
        downloads = self.driver.find_element(*admin_page.navigation.catalog_menu.downloads)
        downloads.click()

    def open_add_new_download(self):
        add_new = self.driver.find_element(*admin_page.products.add_new)
        add_new.click()

    def upload_file(self, file_path):
        input = self.driver.find_element(*admin_page.downloads.upload_input)
        input.send_keys(file_path)

    def get_currencies_titles(self):
        self.driver.find_element(*admin_page.navigation.system).click()
        self.driver.find_element(*admin_page.navigation.system_menu.localisation).click()
        self.driver.find_element(*admin_page.navigation.system_menu.localisation_menu.currencies).click()
        currencies = self.driver.find_elements(*admin_page.currencies.currency_title)
        titles = []
        for currency in currencies:
            titles.append(currency.text)
        return titles
