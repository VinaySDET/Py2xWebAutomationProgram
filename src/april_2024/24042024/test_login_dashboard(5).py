# * explicit_wait(5): you can tell the driver to wait for only a particular element with condition.

import logging
import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_vwo_login_positive():
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

    # < h1
    # class ="page-heading"
    # data-qa="page-heading" >
    # Dashboard
    # < / h1 >
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    wait = WebDriverWait(driver=driver, timeout=10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@data-qa='page-heading']"),"Dashboard"))


    # < span
    # class ="Fw(semi-bold) ng-binding"
    # data-qa="lufexuloga" >
    # Aman
    # < / span >
    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']");
    print(heading_element.text)
    assert heading_element.text == "Aman"

    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
