"""
Fixture for browser to run tests, using selenium webdriver, options, arguments, and additional methods to manage fixture
"""

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.admin_page import AdminPage


class Browser:

    def __init__(self, browser, base_url, imp_wait):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            self.wd = webdriver.Chrome(options=chrome_options)
            self.wd.maximize_window()
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.headless = True
            self.wd = webdriver.Firefox(options=firefox_options)
            self.wd.maximize_window()
        elif browser == 'ie':
            ie_options = webdriver.IeOptions()
            ie_options.add_argument('headless')
            self.wd = webdriver.Ie(options=ie_options)
            self.wd.maximize_window()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.wd.implicitly_wait(int(imp_wait))
        self.base_url = base_url

    def quit(self):
        self.wd.quit()

    def open_homepage(self):
        self.wd.get(self.base_url)

    def open_admin_login_page(self):
        self.wd.get(self.base_url + '/admin')

    def accept_alert(self):
        Alert(self.wd).accept()
        self.wait_success_alert()

    def wait_success_alert(self):
        WebDriverWait(self.wd, 5).until(EC.presence_of_element_located(AdminPage.Products.success_alert))