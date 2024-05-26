from selenium import webdriver
import time
import pytest


def test_open_login():
    driver = webdriver.Chrome()  # POST request - creates the session
    driver.get("https://codewithshani.com/index.php/python-projects/")  # GET request - url parameters
    print(driver.title)
    print(driver.session_id)  # e74e4cc49e13e9cd0539e2f982724c5d
    # print(driver.page_source)
    driver.maximize_window()
    assert driver.title == "Python Projects – CodeWithShani"

    # * NOTE: driver.title: Return the title of the current page i.e., Python Projects – CodeWithShani
    # * NOTE: session id: it'll be like this: c3c5fc6f334bded7b8eed9d713ed8b5a & will be generated in terminal
