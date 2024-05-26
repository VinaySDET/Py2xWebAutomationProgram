import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.positive
@allure.title("Verify that login is working in CURA HEALTH Website")
@allure.description("TC#1 Simple Login check on CURA katalone website.")
def test_idrive360_login_positive():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()

    username = driver.find_element(By.ID, "username")
    username.send_keys("augtest_040823@idrive.com")
    time.sleep(2)

    password = driver.find_element(By.ID, "password")
    password.send_keys("123456")
    time.sleep(2)

    login = driver.find_element(By.ID, "frm-btn")
    login.click()
    # allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type="AttachmentType. PNG")
    time.sleep(5)

    # heading_h5 = driver.find_element(By.TAG_NAME, "h5")
    # assert "Your free trial has expired" in heading_h5.text

    # header_message = driver.find_element(By.XPATH, "//h5[@class='id-card-title']").text
    # print(header_message)
    # assert header_message == "Your free trial has expired", "Error - Invalid message"
    # time.sleep(2)
    # driver.quit()

    msg_element = driver.find_element(By.TAG_NAME, "h5")
    assert msg_element.text == "Your free trial has expired"


    # assert current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error - Invalid URL"

