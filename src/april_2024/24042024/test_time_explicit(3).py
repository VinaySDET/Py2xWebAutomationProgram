# * explicit_wait(5): you can tell the driver to wait for only a particular element, not all the elements with condition

import logging
import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")

    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")

    password_ele = driver.find_element(By.ID, "login-password")
    password_ele.send_keys("Wingify@SDET")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))

    # error _msg: comes after 5 seconds, and I have to wait with some conditions,
    # and i add a condition so that WebDriver should wait for that condition

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg.text)
    assert error_msg.text == "Your email, password, IP address or location did not match"

    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()