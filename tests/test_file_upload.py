"""
Test for file upload function
"""

from page_objects.utils import Utils
from page_objects.admin_login import AdminLogin
from page_objects.admin_page import AdminPage


def test_file_upload(browser):
    file_path = '/home/chaplygin/Downloads/Telegram Desktop/image_2019-09-11_15-22-17.png'
    utils = Utils(browser.wd)
    admin_login = AdminLogin(browser.wd)
    admin_page = AdminPage(browser.wd)
    browser.open_admin_login_page()
    admin_login.fill_username('user')
    admin_login.fill_password('bitnami1')
    admin_login.login()
    admin_page.open_downloads()
    admin_page.open_add_new_download()
    utils.create_file_upload_form()
    admin_page.upload_file(file_path)
    is_file_uploaded = utils.is_file_uploaded()
    assert is_file_uploaded == True