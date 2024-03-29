"""
Fixture for browser to run tests, using selenium webdriver, options, arguments, and additional methods to manage fixture
"""

import allure
from .logger import create_log
import time
from utils.sqlite import Sqlite

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser:

    def __init__(self, browser, base_url, imp_wait, grid, remote):
        if not grid:
            if remote:
                desired_cap = {
                    'browser': 'Chrome',
                    'browser_version': '70.0',
                    'os': 'Windows',
                    'os_version': '7',
                    'resolution': '1024x768',
                    'name': 'Bstack-[Python] Sample Test'
                }
                wd = webdriver.Remote(
                    command_executor='https://bsuser56612:Jzszxyp6daTzocHjpQbA@hub-cloud.browserstack.com/wd/hub',
                    desired_capabilities=desired_cap)
                self.wd = EventFiringWebDriver(wd, MyListener())
            else:
                if browser == "chrome":
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--no-sandbox')
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
        else:
            if browser == "chrome":
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                wd = webdriver.Remote('192.168.0.102:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
                self.wd = EventFiringWebDriver(wd, MyListener())
                self.wd.maximize_window()
            elif browser == "firefox":
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.headless = True
                wd = webdriver.Remote('192.168.0.102:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
                self.wd = EventFiringWebDriver(wd, MyListener())
                self.wd.maximize_window()
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
        self.db_log = Sqlite()

    def on_exception(self, exception, driver):
        #self.db_log.write_log(f'Screenshot path - screenshots/exception-{time.time()}-{exception}.png')
        driver.save_screenshot(f'screenshots/exception-{time.time()}-{exception}.png')
        print(exception)

    def before_find(self, by, value, driver):
        #self.db_log.write_log(f'Finding by - {by}, selector - {value}')
        self.log.info(f'Finding by - {by}, selector - {value}')
        print(by, value)

    def before_click(self, element, driver):
        #self.db_log.write_log(f'Clicking on {element}')
        self.log.info(f'Clicking on {element}')
        print(element)