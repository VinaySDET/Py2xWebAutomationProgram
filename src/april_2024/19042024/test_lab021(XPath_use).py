import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# def test_start_browser():
#     # selenium API - Create session
#     driver = webdriver.Chrome()
#     driver.get("https://katalon-demo-cura.herokuapp.com/")
#     driver.maximize_window()
#     time.sleep(2)


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

    # list_tag= driver.find_element(By.TAG_NAME,"qeyivoyeqa")  //input[contains(@class, 'form-control')]
    # back=list_tag[0]
    # back.click()