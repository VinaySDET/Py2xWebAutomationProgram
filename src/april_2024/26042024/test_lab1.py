import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

# Data Driven Test Case for the Login Page.
# Invalid Login for the VWO Page


@pytest.mark.smoke
@pytest.fixture()
@allure.title("Verify the invalid Login with the Excel Testdata")
@allure.description("TC #1 -10 invalid Login verification for app.vwo.com")
def test_vwo_login(login_username, login_password):   # * made this as parametrized so that i can run multiple times
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")

    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys(login_username)
    #email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")

    password_ele = driver.find_element(By.ID, "login-password")
    password_ele.send_keys(login_password)
    #password_ele.send_keys("Wingify@SDET")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    time.sleep(5)
    result=driver.current_url
    print(result)

    if result !="https://app.vwo.com/#/dashboard":
        print("Invalid Login")
    else:
        print("Valid Login")
    driver.quit()


    # ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    #
    # wait = WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=ignore_list)
    # wait.until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))
    #
    # # * Add a Logic: if we enter the correct username, password -> you will see dashboard page  otherwise error message will be displayed.
    #
    #
    #
    #
    #
    #
    # error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    # print(error_msg.text)
    # assert error_msg.text == "Your email, password, IP address or location did not match"
    # allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
    # driver.quit()