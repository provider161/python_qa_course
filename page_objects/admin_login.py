"""
Class for admin login page
"""

from locators.admin_login import AdminLogin as admin_login


class AdminLogin:

    def __init__(self, driver):
        self.driver = driver

    def fill_username(self, username):
        field = self.driver.find_element(*admin_login.username)
        field.clear()
        field.send_keys(username)

    def fill_password(self, password):
        field = self.driver.find_element(*admin_login.password)
        field.clear()
        field.send_keys(password)

    def login(self):
        button = self.driver.find_element(*admin_login.login_button)
        button.click()
