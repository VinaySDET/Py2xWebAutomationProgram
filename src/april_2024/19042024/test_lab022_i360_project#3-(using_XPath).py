import pytest
import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify login functionality")
@allure.description("Verify if user able to login to idrive360 with valid credentials and redirect on my account page")
def test_idrive360_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    username = "augtest_040823@idrive.com"
    password = "123456"

    driver.get("https://www.idrive360.com/enterprise/login")
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@id='frm-btn']").click()
    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # current_url = driver.current_url
    # assert current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error - Invalid URL"

    # header_message = driver.find_element(By.XPATH, "//h5[@class='id-card-title']")
    # assert header_message.text == "Your free trial has expired", "Error - Invalid message"
    error_message = driver.find_element(By.CSS_SELECTOR, "Your free trial has expired")
    assert "Your free trial has expired" in error_message.text
