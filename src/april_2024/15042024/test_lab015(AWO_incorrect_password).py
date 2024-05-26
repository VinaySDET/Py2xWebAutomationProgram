# 1. Open the browser
# 2. Navigate to URL
# 3. Find the email WebElement and put email id = "abc@gmail.com"
# 4. Find the password input box and enter the password = 123
# 5. Click on the button - sign in
# 6. Verify that the dashboard is loaded - pytest
# 7. Create a report to send to QA Lead - HTML -> Allure Report

import logging
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


# * for incorrect password: Your email, password, IP address or location did not match
# < div
# class ="notification-box-description"
# id="js-notification-box-msg"
# data-qa="rixawilomi"
# >
# Your email, password, IP address or location did not match
# < / div >

def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open the browser
    # navigate to URL-- navigation commands in selenium
    # get(string_url - this command is used to open a specific URL in the browser)... example: driver.get("https://example.com")
    driver.get("https://app.vwo.com/")

    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")

    password_ele = driver.find_element(By.ID, "login-password")
    password_ele.send_keys("Wingify@SDE")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()
    time.sleep(2)

    # * you can use any one assertion out of these 2:  with XPath or without XPath:

    # * assertion using XPath:
    error_msg= driver.find_element(By.XPATH,"//*[text()='Your email, password, IP address or location did not match']")
    # you can use this XPath comand as well: "//div[@id='js-notification-box-msg']"
    print(error_msg.text)
    assert error_msg.text == "Your email, password, IP address or location did not match"
    time.sleep(2)

    # * assertion without using XPath:
    error_msg = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg.text)
    assert error_msg.text == "Your email, password, IP address or location did not match"
    time.sleep(2)

    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)


