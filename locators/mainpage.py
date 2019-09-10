"""
Locators for elements on main page of application. Using selenium By module and css, xpath locators
"""

from selenium.webdriver.common.by import By


class MainPage:

    # search string and button
    search_string = (By.CSS_SELECTOR, '#search input')
    search_button = (By.CSS_SELECTOR, '#search button')

    logo = (By.CSS_SELECTOR, '#logo')

    # cart
    cart_button = (By.CSS_SELECTOR, '#cart button')

    # navigation bar
    desktops = (By.XPATH, '//*[text() = "Desktops"]')
    laptops = (By.XPATH, '//*[text() = "Laptops & Notebooks"]')
    components = (By.XPATH, '//*[text() = "Components"]')
    tablets = (By.XPATH, '//*[text() = "Tablets"]')
    software = (By.XPATH, '//*[text() = "Software"]')
    phones = (By.XPATH, '//*[text() = "Phones & PDAs"]')
    cameras = (By.XPATH, '//*[text() = "Cameras"]')
    mp3 = (By.XPATH, '//*[text() = "MP3 Players"]')

    # promo block
    next_banner = (By.XPATH, "//div[@id='slideshow0']/parent::div//div[@class='swiper-button-next']")
    previous_banner = (By.XPATH, "//div[@id='slideshow0']/parent::div//div[@class='swiper-button-prev']")
    iphone_banner = (By.CSS_SELECTOR, "img[alt='iPhone 6']")
    macbook_banner = (By.CSS_SELECTOR, "img[alt='MacBookAir']")