

def test_check_title(browser):
    browser.open_homepage()
    title = browser.wd.title
    assert title == 'Your Store'
