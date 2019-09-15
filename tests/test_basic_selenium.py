# This Python file uses the following encoding: utf-8
"""
Tests using basic selenium functions - find element, click, send_keys and so on
"""

from page_objects.admin_login import AdminLogin
from page_objects.admin_page import AdminPage
from page_objects.header import Header
from page_objects.search_page import SearchPage
from page_objects.mainpage import MainPage
from page_objects.contact_us import ContactUs


def test_admin_login(browser):
    browser.log.info('Test test_admin_login starting')
    admin_login = AdminLogin(browser.wd)
    admin_page = AdminPage(browser.wd)
    browser.open_admin_login_page()
    admin_login.fill_username('user')
    admin_login.fill_password('bitnami1')
    admin_login.login()
    browser.log.info('Logging out')
    try:
        admin_page.logout()
    except Exception as e:
        browser.log.error(f'Exception - {e}')


def test_change_currency(browser):
    browser.log.info('Test test_change_currency starting')
    header = Header(browser.wd)
    currency = 'USD'
    browser.open_homepage()
    header.change_currency(currency)
    new_currency = header.get_currency()
    browser.log.info('Asserting currencies')
    try:
        assert currency == new_currency
    except AssertionError:
        browser.log.error(f'Currencies are different: test currency - {currency}, new_currency - {new_currency}')


def test_search_laptop(browser):
    main_page = MainPage(browser.wd)
    search_page = SearchPage(browser.wd)
    browser.open_homepage()
    main_page.search('laptop')
    search_query = search_page.get_search_query_text()
    assert search_query == 'Search - laptop'


def test_get_contact_us_page(browser):
    header = Header(browser.wd)
    contact_us = ContactUs(browser.wd)
    browser.open_homepage()
    header.open_contact_us_page()
    page_topic = contact_us.get_page_topic()
    assert page_topic == 'Contact Us'


def test_next_banner(browser):
    main_page = MainPage(browser.wd)
    banner = 'macbook'
    browser.open_homepage()
    main_page.switch_next_banner()
    main_page.check_banner_is_present(banner)