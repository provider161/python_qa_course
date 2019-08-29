"""
Test for selenium action chains, providing drag and drop actions. Test drags document icon and drops it into trash icon
"""

from locators.drag_n_drop import DragNDrop
from selenium.webdriver.common.action_chains import ActionChains


def test_drag_n_drop(browser):
    browser.wd.get('https://code.makery.ch/library/dart-drag-and-drop/')
    frame = browser.wd.find_element(*DragNDrop.i_frame)
    browser.wd.execute_script("arguments[0].scrollIntoView(true);", frame)
    browser.wd.switch_to.frame(frame)
    documents = browser.wd.find_elements(*DragNDrop.document)
    for _ in range(len(documents)):
        trash = browser.wd.find_element(*DragNDrop.trash)
        document = browser.wd.find_element(*DragNDrop.document)
        actions = ActionChains(browser.wd)
        actions.drag_and_drop(document, trash).perform()
