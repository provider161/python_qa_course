"""
Test for file upload function
"""

from page_objects.utils import Utils
from page_objects.admin_login import AdminLogin
from page_objects.admin_page import AdminPage


def test_file_upload(browser):
    utils = Utils(browser.wd)
    admin_login = AdminLogin(browser.wd)
    admin_page = AdminPage(browser.wd)
