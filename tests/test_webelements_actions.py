"""
Tests with web element actions, adding, deleting, editing products in our app.
"""
from locators.admin_page import AdminPage
from locators.admin_login import AdminLogin


def test_add_product(browser):
    browser.open_admin_login_page()
    browser.wd.find_element(*AdminLogin.username).send_keys('user')
    browser.wd.find_element(*AdminLogin.password).send_keys('bitnami1')
    browser.wd.find_element(*AdminLogin.login_button).click()
    browser.wd.find_element(*AdminPage.Navigation.catalog).click()
    browser.wd.find_element(*AdminPage.Navigation.CatalogMenu.products).click()
    browser.wd.find_element(*AdminPage.Products.add_new).click()
    browser.wd.find_element(*AdminPage.Products.AddProduct.product_name).send_keys('new_product')
    browser.wd.find_element(*AdminPage.Products.AddProduct.meta_tag_title).send_keys('new_title')
    browser.wd.find_element(*AdminPage.Products.AddProduct.navigation_data).click()
    browser.wd.find_element(*AdminPage.Products.AddProduct.model).send_keys('new_model')
    browser.wd.find_element(*AdminPage.Products.AddProduct.save).click()
    new_products_list = browser.wd.find_elements(*AdminPage.Products.ProductList.product_in_list)
    new_names = []
    for product in new_products_list:
        name = product.find_element(*AdminPage.Products.ProductList.product_name).text
        new_names.append(name)
    assert 'new_product' in new_names


def test_delete_product(browser):
    browser.open_admin_login_page()
    browser.wd.find_element(*AdminLogin.username).send_keys('user')
    browser.wd.find_element(*AdminLogin.password).send_keys('bitnami1')
    browser.wd.find_element(*AdminLogin.login_button).click()
    browser.wd.find_element(*AdminPage.Navigation.catalog).click()
    browser.wd.find_element(*AdminPage.Navigation.CatalogMenu.products).click()
    product_for_delete = browser.wd.find_element(*AdminPage.Products.ProductList.product_in_list)
    product_for_delete_name = product_for_delete.find_element(*AdminPage.Products.ProductList.product_name).text
    product_for_delete.find_element(*AdminPage.Products.ProductList.checkbox).click()
    browser.wd.find_element(*AdminPage.Products.delete).click()
    browser.accept_alert()
    new_products_list = browser.wd.find_elements(*AdminPage.Products.ProductList.product_in_list)
    new_names = []
    for product in new_products_list:
        name = product.find_element(*AdminPage.Products.ProductList.product_name).text
        new_names.append(name)
    assert product_for_delete_name not in new_names


def test_edit_product(browser):
    browser.open_admin_login_page()
    browser.wd.find_element(*AdminLogin.username).send_keys('user')
    browser.wd.find_element(*AdminLogin.password).send_keys('bitnami1')
    browser.wd.find_element(*AdminLogin.login_button).click()
    browser.wd.find_element(*AdminPage.Navigation.catalog).click()
    browser.wd.find_element(*AdminPage.Navigation.CatalogMenu.products).click()
    product_for_edit = browser.wd.find_element(*AdminPage.Products.ProductList.product_in_list)
    product_for_edit.find_element(*AdminPage.Products.ProductList.edit).click()
    product_name = browser.wd.find_element(*AdminPage.Products.AddProduct.product_name)
    product_name.clear()
    product_name.send_keys('new_edit_product')
    product_title = browser.wd.find_element(*AdminPage.Products.AddProduct.meta_tag_title)
    product_title.clear()
    product_title.send_keys('new_edit_title')
    browser.wd.find_element(*AdminPage.Products.AddProduct.navigation_data).click()
    product_model = browser.wd.find_element(*AdminPage.Products.AddProduct.model)
    product_model.clear()
    product_model.send_keys('new_edit_model')
    browser.wd.find_element(*AdminPage.Products.AddProduct.save).click()
    new_products_list = browser.wd.find_elements(*AdminPage.Products.ProductList.product_in_list)
    new_names = []
    for product in new_products_list:
        name = product.find_element(*AdminPage.Products.ProductList.product_name).text
        new_names.append(name)
    assert 'new_edit_product' in new_names
