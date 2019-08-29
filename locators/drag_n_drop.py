"""
Locators for drag'n'drop page and test
"""
from selenium.webdriver.common.by import By


class DragNDrop:

    i_frame = (By.CSS_SELECTOR, 'iframe')
    document = (By.CSS_SELECTOR, '.document')
    trash = (By.CSS_SELECTOR, '.trash')