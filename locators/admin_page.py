"""
Locators for elements on admin page of application. Using selenium By module and css, xpath locators
"""
from selenium.webdriver.common.by import By


class AdminPage:

    logout = (By.CSS_SELECTOR, '.fa.fa-sign-out')

    class navigation:

        catalog = (By.CSS_SELECTOR, '#menu-catalog a')
        system = (By.CSS_SELECTOR, '#menu-system a')

        class catalog_menu:

            products = (By.XPATH, '//*[@id="menu-catalog"]//*[text() = "Products"]')
            downloads = (By.XPATH, '//*[@id="menu-catalog"]//*[text() = "Downloads"]')

        class system_menu:

            localisation = (By.XPATH, '//*[@id="menu-system"]//*[text() = "Localisation"]')

            class localisation_menu:

                currencies = (By.XPATH, '//*[@id="menu-system"]//*[text() = "Currencies"]')

    class currencies:

        currency_title = (By.XPATH, "//form[@id='form-currency']//tbody/tr/td[2]")

    class products:

        add_new = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
        copy = (By.CSS_SELECTOR, 'button[data-original-title="Copy"]')
        delete = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
        success_alert = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')

        class product_list:

            product_in_list = (By.CSS_SELECTOR, '.table-responsive tbody tr')
            checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
            edit = (By.CSS_SELECTOR, 'a[data-original-title="Edit"]')
            product_name = (By.XPATH, './/td[@class="text-left"][1]')

        class add_product:

            save = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')

            # product description
            product_name = (By.CSS_SELECTOR, '#input-name1')
            meta_tag_title = (By.CSS_SELECTOR, '#input-meta-title1')
            model = (By.CSS_SELECTOR, '#input-model')

            # navigation bookmarks
            navigation_data = (By.XPATH, '//*[text() = "Data"]')
            navigation_general = (By.XPATH, '//*[text() = "General"]')

    class downloads:

        upload_input = (By.CSS_SELECTOR, 'input[type=file]')