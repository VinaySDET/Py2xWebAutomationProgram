# * Fluent Wait(): defines the max amount of time to wait for a condition as well as the frequency with which to check the condition

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


@pytest.mark.smoke
@allure.title("Verify the Login is working in app.vwo.com website")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("TC#1 - Simple Login check on app,vwo website")
@allure.issue("")
def test_start_browser_negative():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")

    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")

    password_ele = driver.find_element(By.ID, "login-password")
    password_ele.send_keys("Wingify@SDE")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

    wait = WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=ignore_list)
    wait.until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg.text)
    assert error_msg.text == "Your email, password, IP address or location did not match"

@pytest.mark.smoke
@allure.title("Verify the Login is working in app.vwo.com website")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("TC#1 - Simple Login check on app,vwo website")
@allure.issue("")
def test_start_browser_positive():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")

    email_address = driver.find_element(By.ID, "login-username")
    email_address.send_keys("contact+atb5x@thetestingacademy.com")

    password = driver.find_element(By.ID, "login-password")
    password.send_keys("Wingify@SDET")

    button_submit = driver.find_element(By.ID, "js-login-btn")
    button_submit.click()

    ignored_list = [ElementNotVisibleException, ElementNotSelectableException]

    wait = WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=ignored_list)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-qa='lufexuloga']")))

    error_msg_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    print(error_msg_element.text)
    assert error_msg_element.text == "Aman"

    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
