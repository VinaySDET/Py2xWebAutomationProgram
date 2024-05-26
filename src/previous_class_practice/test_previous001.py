import pytest
from selenium import webdriver


@pytest.fixture()
def start_browser():
    driver = webdriver.Chrome()
    # yield driver
    return driver


# yield and return both are same
# yield: it only runs when a driver is available, it gives you the value of the driver & the value is webdriver.Chrome()
# return: value will be stored permanently

def test_open_url_verify_title(start_browser):
    start_browser.get("https://codewithshani.com/index.php/python-projects/")
    print(start_browser.title)
    start_browser.maximize_window()
    #  verification means Actual Result == Expected Resul
    assert start_browser.title == "Python Projects – CodeWithShani"
