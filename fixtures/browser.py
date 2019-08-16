"""
Fixture for browser to run tests, using selenium webdriver, options, arguments, and additional methods to manage fixture
"""

from selenium import webdriver


class Browser:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            self.wd = webdriver.Chrome(options=chrome_options)
            self.wd.maximize_window()
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument('headless')
            self.wd = webdriver.Firefox(options=firefox_options)
            self.wd.maximize_window()
        elif browser == 'ie':
            ie_options = webdriver.IeOptions()
            ie_options.add_argument('headless')
            self.wd = webdriver.Ie(options=ie_options)
            self.wd.maximize_window()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.wd.implicitly_wait(60)
        self.base_url = base_url

    def quit(self):
        self.wd.quit()

    def open_homepage(self):
        self.wd.get(self.base_url)
