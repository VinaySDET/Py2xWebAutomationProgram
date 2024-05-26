# 1. Open the browser
# 2. Navigate to a URL
# 3. Find the email WebElement and put email id = "abc@gmail.com"
# 4. Find the password input box and enter the password = 123
# 5. Click on the button - sign in
# 6. Verify that after login the dashboard page is loaded - pytest
# 7. create a report to send to QA Lead - HTML -> Allure Report

import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open the browser
    # navigate to URL-- navigation commands in selenium
    # get(string_url - this command is used to open a specific URL in the browser)... example: driver.get("https://example.com")
    driver.get("https://app.vwo.com/")
    assert driver.title == "Login - VWO"

    #  * username or email address
    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    #  * password
    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # aria-autocomplete="list"
    # >

    # * sign in button
    # < button
    # type = "submit"
    # id = "js-login-btn"
    # class ="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica"
    # >
    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.ID, "login-password")
    log_in_ele = driver.find_element(By.ID, "js-login-btn")

    # # sending the data -? email & password -> clicking on the button
    # # sendkeys and click()
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")
    password_ele.send_keys("Wingify@SDET")
    log_in_ele.click()
    time.sleep(5)

    logger = logging.getLogger(__name__)
    logger.info('title is - ' + driver.title)
    assert "Dashboard" in driver.title

    # *6. Verify that the dashboard page is loaded after Log in- pytest
    assert driver.title == "Dashboard"

    # * verify the change URL after Log in - using assert
    assert driver.current_url == "https://app.vwo.com/#/dashboard"
