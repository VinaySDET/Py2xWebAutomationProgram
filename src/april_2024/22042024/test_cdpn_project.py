# Selenium Mini project #3

# 1. Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
# 2. Enter all the fields excepts the username
# 3. Verify that the error message comes when you click on the submit button.

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@pytest.mark.smoke
@allure.title("Verify that login to IDrive 360 is working fine")
@allure.description("TC #1 - Simple Login Check on Idrive 360 Website")
def test_cdpn():
    drive = webdriver.Chrome()
    drive.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    drive.maximize_window()
    drive.switch_to.frame(drive.find_element(By.ID, "result"))
    # < input
    # type = "text"
    # id = "email"
    # placeholder = "Enter email"
    # >
    email_element = drive.find_element(By.ID,"email")
    email_element.send_keys("test@gmail.com")
    time.sleep(2)

    # < input
    # type = "password"
    # id = "password"
    # placeholder = "Enter password"
    # >
    pwd_element = drive.find_element(By.ID,"password")
    pwd_element.send_keys("123456")
    time.sleep(2)

    # < input
    # type = "password"
    # id = "password2"
    # placeholder = "Enter password again"
    # >
    cnf_pwd_element = drive.find_element(By.ID, "password2")
    cnf_pwd_element.send_keys("123456")
    time.sleep(2)

    # < button >
    # Submit
    # < / button >
    submit_element = drive.find_element(By.XPATH,"//button[text()='Submit']")
    submit_element.click()
    time.sleep(2)

    # < input
    # type = "text"
    # id = "username"
    # placeholder = "Enter Username"
    # >
    msg_element = drive.find_element(By.XPATH, "//input[@id='username']/following::small")
    #msg_element=drive.find_element(By.ID,"username")
    assert msg_element.text == "Username must be at least 3 characters"
    # allure.attach(drive.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)