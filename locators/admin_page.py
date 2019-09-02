"""
Locators for elements on admin page of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class AdminPage:

    logout = (By.CSS_SELECTOR, '.fa.fa-sign-out')

    class Navigation:

        catalog = (By.CSS_SELECTOR, '#menu-catalog a')

        class CatalogMenu:

            products = (By.XPATH, '//*[@id="menu-catalog"]//*[text() = "Products"]')

    class Products:

        add_new = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
        copy = (By.CSS_SELECTOR, 'button[data-original-title="Copy"]')
        delete = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
        success_alert = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')

        class ProductList:

            product_in_list = (By.CSS_SELECTOR, '.table-responsive tbody tr')
            checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
            edit = (By.CSS_SELECTOR, 'a[data-original-title="Edit"]')
            product_name = (By.XPATH, './/td[@class="text-left"][1]')

        class AddProduct:

            save = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')

            # product description
            product_name = (By.CSS_SELECTOR, '#input-name1')
            meta_tag_title = (By.CSS_SELECTOR, '#input-meta-title1')
            model = (By.CSS_SELECTOR, '#input-model')

            # navigation bookmarks
            navigation_data = (By.XPATH, '//*[text() = "Data"]')
            navigation_general = (By.XPATH, '//*[text() = "General"]')