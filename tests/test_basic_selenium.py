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


def test_admin_login(browser):
    browser.open_admin_login_page()
    browser.wd.find_element(*AdminLogin.username).send_keys('user')
    browser.wd.find_element(*AdminLogin.password).send_keys('bitnami1')
    browser.wd.find_element(*AdminLogin.login_button).click()
    browser.wd.find_element(*AdminPage.logout)


def test_change_currency(browser):
    browser.open_homepage()
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