"""
Class for additional tools and utilities, helpers
"""
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.admin_page import AdminPage


class Utils:

    def __init__(self, driver):
        self.driver = driver

    def accept_alert(self):
        Alert(self.driver).accept()
        self.wait_success_alert()

    def wait_success_alert(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(AdminPage.products.success_alert))

    def create_file_upload_form(self):
        self.driver.execute_script("""
        var form = document.createElement("form");
        form.id = "form-upload";
        form.style.display = "block";
        form.enctype = "multipart/form-data";
        input = document.createElement("input");
        input.type = "file";
        input.name = "file";
        form.appendChild(input);
        body = document.getElementsByTagName("body")[0];
        body.insertBefore(form, body.firstChild);
        """)

    def is_file_uploaded(self):
        uploaded_file = self.driver.find_element(*AdminPage.downloads.upload_input).get_attribute('value')
        return True if uploaded_file else False