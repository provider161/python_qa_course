"""
Tests with web element actions, adding, deleting, editing products in our app.
"""
from locators.admin_page import AdminPage
from locators.admin_login import AdminLogin
from locators.product import Product

from page_objects.utils import Utils

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product(browser):
    browser.open_admin_login_page()
    browser.wd.find_element(*AdminLogin.username).send_keys('user')
    browser.wd.find_element(*AdminLogin.password).send_keys('bitnami1')
    browser.wd.find_element(*AdminLogin.login_button).click()
    WebDriverWait(browser.wd, 5).until(EC.title_is('Dashboard'))
    browser.wd.find_element(*AdminPage.navigation.catalog).click()
    browser.wd.find_element(*AdminPage.navigation.catalog_menu.products).click()
    browser.wd.find_element(*AdminPage.products.add_new).click()
    WebDriverWait(browser.wd, 5).until(EC.visibility_of_element_located(Product.add_product_title))
    browser.wd.find_element(*AdminPage.products.add_product.product_name).send_keys('new_product')
    browser.wd.find_element(*AdminPage.products.add_product.meta_tag_title).send_keys('new_title')
    browser.wd.find_element(*AdminPage.products.add_product.navigation_data).click()
    browser.wd.find_element(*AdminPage.products.add_product.model).send_keys('new_model')
    browser.wd.find_element(*AdminPage.products.add_product.save).click()
    browser.wait_success_alert()
    new_products_list = browser.wd.find_elements(*AdminPage.products.product_list.product_in_list)
    new_names = []
    for product in new_products_list:
        name = product.find_element(*AdminPage.products.product_list.product_name).text
        new_names.append(name)
    assert 'new_product' in new_names


def test_delete_product(browser):
    utils = Utils(browser.wd)
    browser.open_admin_login_page()
    browser.wd.find_element(*AdminLogin.username).send_keys('user')
    browser.wd.find_element(*AdminLogin.password).send_keys('bitnami1')
    browser.wd.find_element(*AdminLogin.login_button).click()
    WebDriverWait(browser.wd, 5).until(EC.title_is('Dashboard'))
    browser.wd.find_element(*AdminPage.navigation.catalog).click()
    browser.wd.find_element(*AdminPage.navigation.catalog_menu.products).click()
    product_for_delete = browser.wd.find_element(*AdminPage.products.product_list.product_in_list)
    product_for_delete_name = product_for_delete.find_element(*AdminPage.products.product_list.product_name).text
    product_for_delete.find_element(*AdminPage.products.product_list.checkbox).click()
    browser.wd.find_element(*AdminPage.products.delete).click()
    utils.accept_alert()
    new_products_list = browser.wd.find_elements(*AdminPage.products.product_list.product_in_list)
    new_names = []
    for product in new_products_list:
        name = product.find_element(*AdminPage.products.product_list.product_name).text
        new_names.append(name)
    assert product_for_delete_name not in new_names


def test_edit_product(browser):
    browser.open_admin_login_page()
    browser.wd.find_element(*AdminLogin.username).send_keys('user')
    browser.wd.find_element(*AdminLogin.password).send_keys('bitnami1')
    browser.wd.find_element(*AdminLogin.login_button).click()
    WebDriverWait(browser.wd, 5).until(EC.title_is('Dashboard'))
    browser.wd.find_element(*AdminPage.navigation.catalog).click()
    browser.wd.find_element(*AdminPage.navigation.catalog_menu.products).click()
    product_for_edit = browser.wd.find_element(*AdminPage.products.product_list.product_in_list)
    product_for_edit.find_element(*AdminPage.products.product_list.edit).click()
    WebDriverWait(browser.wd, 5).until(EC.visibility_of_element_located(Product.edit_product_title))
    product_name = browser.wd.find_element(*AdminPage.products.add_product.product_name)
    product_name.clear()
    product_name.send_keys('new_edit_product')
    product_title = browser.wd.find_element(*AdminPage.products.add_product.meta_tag_title)
    product_title.clear()
    product_title.send_keys('new_edit_title')
    browser.wd.find_element(*AdminPage.products.add_product.navigation_data).click()
    product_model = browser.wd.find_element(*AdminPage.products.add_product.model)
    product_model.clear()
    product_model.send_keys('new_edit_model')
    browser.wd.find_element(*AdminPage.products.add_product.save).click()
    browser.wait_success_alert()
    new_products_list = browser.wd.find_elements(*AdminPage.products.product_list.product_in_list)
    new_names = []
    for product in new_products_list:
        name = product.find_element(*AdminPage.products.product_list.product_name).text
        new_names.append(name)
    assert 'new_edit_product' in new_names
