# Selenium Mini project #4

# 1. Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
# 2. Enter all the fields except username
# 3. Verify that the error message comes when you click on the submit button.

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@pytest.mark.smoke
@allure.title("Verify that the error message comes when you click on the submit button.")
@allure.description("TC #1 - Simple Login Check on cdpn.io Website")
def test_cdpn_io():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()

    # * use anyone locator either ID or XPATH to use iframe
    #driver.switch_to.frame(driver.find_element(By.ID, "result"))
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='result']"))
    time.sleep(2)

    #< input type = "text"
    # id = "username"
    # placeholder = "Enter Username"
    # >
    user = driver.find_element(By.XPATH, "//input[@id='username']")
    user.send_keys("vt")
    time.sleep(2)

    # < input
    # type = "text"
    # id = "email"
    # placeholder = "Enter email"
    # >
    email_element = driver.find_element(By.ID,"email")
    email_element.send_keys("test@gmail.com")
    time.sleep(2)

    # < input
    # type = "password"
    # id = "password"
    # placeholder = "Enter password"
    # >
    pwd_element = driver.find_element(By.ID,"password")
    pwd_element.send_keys("123456")
    time.sleep(2)

    # < input
    # type = "password"
    # id = "password2"
    # placeholder = "Enter password again"
    # >
    cnf_pwd_element = driver.find_element(By.ID, "password2")
    cnf_pwd_element.send_keys("123456")
    time.sleep(2)

    # < button >
    # Submit
    # < / button >
    submit_element = driver.find_element(By.XPATH,"//button[text()='Submit']")
    submit_element.click()
    time.sleep(2)

    # < input
    # type = "text"
    # id = "username"
    # placeholder = "Enter Username"
    # >
    msg_element = driver.find_element(By.XPATH, "//input[@id='username']/following::small")
    assert msg_element.text == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)