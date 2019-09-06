"""
Class for header block, located on the whole application pages
"""

from locators.header import Header as header


class Header:

    def __init__(self, driver):
        self.driver = driver

    def change_currency(self, currency):
        currency_button = self.driver.find_element(*header.currency_button)
        currency_button.click()
        if currency == 'EUR':
            euro_button = self.driver.find_element(*header.currency_euro)
            euro_button.click()
        elif currency == 'USD':
            usd_button = self.driver.find_element(*header.currency_dollar)
            usd_button.click()
        elif currency == 'GBP':
            gbp_button = self.driver.find_element(*header.currency_pound)
            gbp_button.click()

    def get_currency(self):
        currency = self.driver.find_element(*header.current_currency)
        return currency.text
