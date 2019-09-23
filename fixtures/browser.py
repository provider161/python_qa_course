"""
Fixture for browser to run tests, using selenium webdriver, options, arguments, and additional methods to manage fixture
"""

import allure
from .logger import create_log
import time

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class Browser:

    def __init__(self, browser, base_url, imp_wait):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            wd = webdriver.Chrome(options=chrome_options)
            self.wd = EventFiringWebDriver(wd, MyListener())
            self.wd.maximize_window()
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.headless = True
            wd = webdriver.Firefox(options=firefox_options)
            self.wd = EventFiringWebDriver(wd, MyListener())
            self.wd.maximize_window()
        elif browser == 'ie':
            ie_options = webdriver.IeOptions()
            ie_options.add_argument('headless')
            wd = webdriver.Ie(options=ie_options)
            self.wd = EventFiringWebDriver(wd, MyListener())
            self.wd.maximize_window()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.wd.implicitly_wait(int(imp_wait))
        self.base_url = base_url
        self.log = create_log()

    def quit(self):
        self.log.info('Closing browser')
        self.wd.quit()

    def open_homepage(self):
        with allure.step('Opening homepage'):
            self.log.info('Opening homepage')
            self.wd.get(self.base_url)

    def open_admin_login_page(self):
        with allure.step('Opening adminpage'):
            self.log.info('Opening adminpage')
            self.wd.get(self.base_url + '/admin')


class MyListener(AbstractEventListener):

    def __init__(self, *args, **kwargs):
        self.log = create_log()
        super().__init__(*args, **kwargs)

    def on_exception(self, exception, driver):
        driver.save_screenshot(f'screenshots/exception-{time.time()}-{exception}.png')
        print(exception)

    def before_find(self, by, value, driver):
        self.log.info(f'Finding by - {by}, selector - {value}')
        print(by, value)

    def before_click(self, element, driver):
        self.log.info(f'Clicking on {element}')
        print(element)