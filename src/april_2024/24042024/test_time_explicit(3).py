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
    time.sleep(5)

    # * command-1: presence_of_element_located

    WebDriverWait(driver=driver, timeout=10).until(
        EC.presence_of_element_located((By.ID, "js-notification-box-msg")))

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg.text)
    assert error_msg.text == "Your email, password, IP address or location did not match"


def test_start_browser_positive():
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


    # * we have so many EC commands:
    # * text_to_be_present_in_element
    # * visibility_of_element_located
    # * presence_of_element_located
    # * element_to_be_clickable
    # * element_to_be_selected
    # * element_located_to_be_selected
    # * staleness_of
    # * element_to_be_visible
    # * element_located_to_be_visible
    # * invisibility_of_element_located
    # * element_to_be_enabled
    # * element_located_to_be_enabled
    # * frame_to_be_available_and_switch_to_it
    # * invisibility_of_element_located
    # * element_to_be_selected
    # * element_located_to_be_selected
    # * element_selection_state_to_be

    # * command-2: text_to_be_present_in_element

    # WebDriverWait(driver=driver, timeout=10).until(
    #     EC.text_to_be_present_in_element((By.XPATH, "//span[@data-qa='lufexuloga']"),
    #                                                                                 "Aman"))
    #
    # error_msg = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    # print(error_msg.text)
    # assert error_msg.text == "Aman"

    # * command-3: visibility_of_element_located

    WebDriverWait(driver=driver, timeout=10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-qa='lufexuloga']")))

    error_msg = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    print(error_msg.text)
    assert error_msg.text == "Aman"

    # error _msg: comes after 10 seconds, and I have to wait with some conditions,
    # and i add a condition so that WebDriver should wait for that condition
    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
