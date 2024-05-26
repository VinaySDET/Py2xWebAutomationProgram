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
    #assert driver.title == "Login - VWO"

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

def test_free_trial():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open the browser
    # navigate to URL-- navigation commands in selenium
    # get(string_url - this command is used to open a specific URL in the browser)... example: driver.get("https://example.com")
    driver.get("https://app.vwo.com/")

    # * start a free trial: this is an anchor tag and we can use on both LINK_TEXT and PARTIAL_TEXT
    # < a
    # href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class ="text-link"
    # data-qa="bericafeqo"
    # >
    # Start a free trial
    # < / a >
    #
    # * LINK_TEXT: if we know the full link
    link = driver.find_element(By.LINK_TEXT, "Start a free trial")
    link.click()


def test_Sign_in_SSO():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open the browser
    # navigate to URL-- navigation commands in selenium
    # get(string_url - this command is used to open a specific URL in the browser)... example: driver.get("https://example.com")
    driver.get("https://app.vwo.com/")

    # * Sign in using SSO: this is not  an anchor tag, it's a button
    # <
    # button
    # type = "button"
    # class ="btn btn--link btn--primary Td(u)"
    # onclick="login.goToSSOView()"
    # data-qa="dobevozose"
    # >
    # Sign in using SSO
    # < / button >
    #
    # link = driver.find_element(By.LINK_TEXT, "Sign in using SSO")
    # link.click()

    # SSO_id = driver.find_element(By.XPATH, "//input[text()=  'Sign in using SSO']")
    # SSO_id.click()
    driver.find_element(By.XPATH,"//button[@class='btn btn--link btn--primary Td(u)']").click()
    time.sleep(5)

    # < input type = "email"
    # class ="text-input login-email-input W(100%)"
    # name="username"
    # id="sso-email"
    # data-qa="gakifiqexa"
    # data-gtm-form-interact-field-id="1" >

    username = driver.find_element(By.ID, "sso-email")
    username.send_keys("contact+atb5x@thetestingacademy.com")
    time.sleep(2)

    # < span
    # data-qa="ijomuafafk" >
    # Sign in < / span >

    driver.find_element(By.XPATH, "//*[@data-qa='ijomuafafk']").click()
    time.sleep(5)

    # < button
    # type = "button"
    # class ="btn btn--link"
    # onclick="login.gotoLoginView()"
    # data-qa="qeyivoyeqa"
    # fdprocessedid="nhz8a" >
    # « Back
    # < / button >

    driver.find_element(By.XPATH, "//*[@data-qa='yatuzudoto']").click()
    time.sleep(5)
