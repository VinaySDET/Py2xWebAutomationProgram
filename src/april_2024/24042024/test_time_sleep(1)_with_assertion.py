# * time.sleep(5): i am telling to python interpreter to wait for 5 seconds

import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()

    # * open the browser
    driver.get("https://app.vwo.com/")

    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")

    password_ele = driver.find_element(By.ID, "login-password")
    password_ele.send_keys("Wingify@SDET")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    time.sleep(2)
    button_submit_element.click()
    time.sleep(5)

    # # * condition for verifying an error message for a negative test case: 1. set wrong password 2. set error message
    # error_message=driver.find_element(By.XPATH,"//div[@id='js-notification-box-msg']")
    # print(error_message)
    # assert error_message.text == "Your email, password, IP address or location did not match"

    # * condition for verifying an error message for a positive test case: 1. set correct password 2. set blank message
    error_message = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
    print(error_message)
    assert error_message.text == ""

    # * time.sleep(5) :
    # telling to python interpreter to wait for 5 seconds before continuing to log in.
