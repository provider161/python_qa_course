# This Python file uses the following encoding: utf-8
"""
Tests using basic selenium functions - find element, click, send_keys and so on
"""

from locators.admin_page import AdminPage
from locators.admin_login import AdminLogin
from locators.product import Product
from locators.mainpage import MainPage
from locators.header import Header
from locators.footer import Footer
from locators.search_page import SearchPage
from locators.contact_us import ContactUs

from page_objects.admin_login import AdminLogin
from page_objects.admin_page import AdminPage
from page_objects.header import Header


def test_admin_login(browser):
    admin_login = AdminLogin(browser.wd)
    admin_page = AdminPage(browser.wd)
    browser.open_admin_login_page()
    admin_login.fill_username('user')
    admin_login.fill_password('bitnami1')
    admin_login.login()
    admin_page.logout()


def test_change_currency(browser):
    header = Header(browser.wd)
    currency = 'EUR'
    browser.open_homepage()
    header.change_currency(currency)
    browser.wd.find_element(*Header.currency_button).click()
    browser.wd.find_element(*Header.currency_euro).click()
    assert browser.wd.find_element(*Header.current_currency).text == u"\u20AC"


def test_search_laptop(browser):
    browser.open_homepage()
    browser.wd.find_element(*MainPage.search_string).send_keys('laptop')
    browser.wd.find_element(*MainPage.search_button).click()
    search_query = browser.wd.find_element(*SearchPage.search_query).text
    assert search_query == 'Search - laptop'


def test_get_contact_us_page(browser):
    browser.open_homepage()
    browser.wd.find_element(*Header.contacts).click()
    page_topic = browser.wd.find_element(*ContactUs.page_topic).text
    assert page_topic == 'Contact Us'


def test_next_banner(browser):
    browser.open_homepage()
    browser.wd.find_element(*MainPage.next_banner).click()
    browser.wd.find_element(*MainPage.macbook_banner)