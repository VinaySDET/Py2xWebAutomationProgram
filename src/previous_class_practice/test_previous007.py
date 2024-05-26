import pytest
from selenium import webdriver
import logging


@pytest.fixture()
def start_browser():
    driver = webdriver.Chrome()
    # yield driver
    return driver


# yield and return both are same
# yield: it only runs when a driver is available, it gives you the value of the driver & the value is webdriver.Chrome()
# return: value will be stored permanently

def test_open_url_verify_title(start_browser):
    logger = logging.getLogger(__name__)
    start_browser.get("https://app.vwo.com/")
    print(start_browser.title)
    start_browser.maximize_window()
    logger.info("This is Information Logs")
    logger.warning("This is Warning Logs")
    logger.error("This is  Error Logs")
    logger.critical("This is Critical Logs")
    #  verification means Actual Result == Expected Resul
    assert start_browser.title == "Login - VWO"
