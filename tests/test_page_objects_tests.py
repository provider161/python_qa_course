"""
Tests using Page Objects pattern
"""

from page_objects.mainpage import MainPage
from page_objects.header import Header
from page_objects.product import Product
from page_objects.search_page import SearchPage


def test_open_tablets_category(browser):
    main_page = MainPage(browser.wd)
    browser.open_homepage()
    main_page.open_tablets_category()
    title = main_page.get_category_title()
    assert title == 'Tablets'


def test_open_shopping_cart(browser):
    header = Header(browser.wd)
    main_page = MainPage(browser.wd)
    browser.open_homepage()
    header.open_shopping_cart()
    status = main_page.get_shopping_cart_status()
    assert status == 'Your shopping cart is empty!'


def test_check_product_price(browser):
    main_page = MainPage(browser.wd)
    product = Product(browser.wd)
    browser.open_homepage()
    main_page.open_cameras_category()
    main_page.select_first_product()
    price = product.get_price()
    assert price == '$98.00'


def test_change_products_view(browser):
    main_page = MainPage(browser.wd)
    browser.open_homepage()
    main_page.open_cameras_category()
    main_page.select_grid_view()
    is_grid_view = main_page.is_grid_view()
    assert is_grid_view == True


def test_search_canon(browser):
    main_page = MainPage(browser.wd)
    search_page = SearchPage(browser.wd)
    browser.open_homepage()
    main_page.search('canon')
    product_name = search_page.get_first_result_product_name()
    assert product_name == 'Canon EOS 5D'