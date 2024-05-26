from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@pytest.mark.smoke
@allure.title("Verify that login to IDrive 360 is working fine")
@allure.description("TC #1 - Simple Login Check on Idrive 360 Website")
def test_task2():
    drive = webdriver.Chrome()
    drive.get("https://www.idrive360.com/enterprise/login")
    drive.maximize_window()
    email_element = drive.find_element(By.ID,"username")
    email_element.send_keys("augtest_040823@idrive.com")
    pwd_element = drive.find_element(By.ID,"password")
    pwd_element.send_keys("123456")
    submit_button = drive.find_element(By.ID,"frm-btn")
    submit_button.click()
    time.sleep(10)
    assert drive.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error Message 1"
    msg_element = drive.find_element(By.CLASS_NAME,"id-card-title")
    assert msg_element.text == "Your free trial has expired"
    allure.attach(drive.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)