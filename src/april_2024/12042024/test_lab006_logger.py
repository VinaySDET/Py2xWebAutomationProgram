from selenium import webdriver
import time
import pytest
import logging


def test_open_login():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()  # POST request - creates the session
    driver.get("https://codewithshani.com/index.php/python-projects/")  # GET request - url parameters
    driver.maximize_window()
    print(driver.title)
    LOGGER.info(driver.title)
    assert driver.title == "Python Projects – CodeWithShani"

