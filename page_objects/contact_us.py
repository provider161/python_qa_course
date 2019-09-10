"""
Class for application contact us description.
Contains methods to interact with page parts, elements, get page information
"""

from locators.contact_us import ContactUs as contact_us


class ContactUs:

    def __init__(self, driver):
        self.driver = driver

    def get_page_topic(self):
        page_topic = self.driver.find_element(*contact_us.page_topic)
        return page_topic.text