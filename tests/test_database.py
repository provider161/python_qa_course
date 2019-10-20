"""
Test to check database work, add data to database and verify it with selenium
"""

from page_objects.admin_login import AdminLogin
from page_objects.admin_page import AdminPage


def test_database(db, browser):
    db.add_currency()
    admin_login = AdminLogin(browser.wd)
    admin_page = AdminPage(browser.wd)
    browser.open_admin_login_page()
    admin_login.fill_username('user')
    admin_login.fill_password('bitnami1')
    admin_login.login()
    titles = admin_page.get_currencies_titles()
    db.delete_currency()
    assert 'test' in titles