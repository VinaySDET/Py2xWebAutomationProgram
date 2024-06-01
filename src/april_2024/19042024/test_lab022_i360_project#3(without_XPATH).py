# * 1. Open the url: https://www.idrive360.com/enterprise/login/
# * 2. Enter the username, password
# * 3. Verify that Trial finished and current URL also
# * 4. Add a logic to add allure screen for the Trial end.


import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Verify that login is working in IDrive360 website")
@allure.description(
    "TC#1 - Verify if user able to login to idrive360 with valid credentials and redirect on my account page.")
def test_i360_positive():
    logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login/")
    driver.maximize_window()

    # * verify the change URL - using assertion
    curr_url = driver.current_url
    assert curr_url == "https://www.idrive360.com/enterprise/login"
    time.sleep(2)

    # < input ngcontent - yqn - c4 = ""
    # autofocus = ""
    # class ="id-form-ctrl ng-valid ng-touched ng-dirty"
    # id="username"
    # name="username"
    # type="email" >

    username = driver.find_element(By.ID, "username")
    username.send_keys("augtest_040823@idrive.com")
    time.sleep(2)

    # < input_ngcontent - yqn - c4 = ""
    # class ="id-form-ctrl ng-valid ng-dirty ng-touched"
    # id="password"
    # name="password"
    # tabindex="0"
    # type="password" >

    password = driver.find_element(By.ID, "password")
    password.send_keys("123456")
    time.sleep(2)

    # < a
    # ngcontent - hrm - c4 = ""
    # class ="id-hide-pwd"
    # href="javascript:;"
    # tabindex="0" >
    # Show
    # < / a >
    show_pwd = driver.find_element(By.LINK_TEXT, "Show")
    show_pwd.click()
    time.sleep(2)

    # < span
    # ngcontent - hrm - c4 = ""
    # class ="id-checkmark"
    # tabindex="-1" >
    # < / span >

    remember_me = driver.find_element(By.CLASS_NAME, "id-checkmark")
    remember_me.click()
    time.sleep(2)

    # < button_ngcontent - yqn - c4 = ""
    # class ="id-btn id-info-btn-frm"
    # id="frm-btn"
    # type="submit" >
    # Sign in
    # < / button >
    login = driver.find_element(By.ID, "frm-btn")
    login.click()
    # allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type="AttachmentType. PNG")
    time.sleep(15)

    # # * verify the change URL - using assert
    change_url = driver.current_url
    assert change_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error - Invalid URL"
    time.sleep(15)

    # < div_ngcontent - xnn - c10 = ""
    # class ="id-card-blk id-expire-msg id-expire-msg-nw failure"
    # id="expiredmsg" >
    # < div _ngcontent-xnn-c10=""
    # class ="id-card-cont" >
    # < i _ngcontent-xnn-c10=""
    # class ="id-expire-msg-icon" >
    # < / i >
    # < h5 _ngcontent-xnn-c10=""
    # class ="id-card-title" >
    # Your free trial has expired
    # < / h5 >
    # < p _ngcontent-xnn-c10="" >
    # and your account has been canceled.
    # < / p >
    # < p _ngcontent-xnn-c10="" >
    # In order to reactivate your account, upgrade your account and save 25 % *.
    # < / p >
    # < / div >
    # < / div >

    # < h5_ngcontent - xnn - c10 = ""
    # class ="id-card-title" >
    # Your free trial has expired
    # < / h5 >

    # * you can use any locators, either TAG_NAME or CLASS_NAME
    heading_h5 = driver.find_element(By.TAG_NAME, "h5")
    #heading_h5= driver.find_element(By.CLASS_NAME, "id-card-title")
    assert "Your free trial has expired" in heading_h5.text
    assert driver.title == "IDrive 360 account details"
    print(heading_h5)
    print(driver.title)
    time.sleep(12)

    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # assert expiredmsg.text == "Your free trial has expired\nand your account has been canceled.\nIn order to reactivate your account, upgrade your account and save 25 % *.", "Assertion- Fail Message #3 -Enter wrong URL(Appointment)"
