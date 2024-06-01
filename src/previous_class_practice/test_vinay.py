from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import allure


def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    first_name=driver.find_elements(By.XPATH,"//input[@name='firstname']")

    # * to use an action class, you have to create an object of an action chain
    actions=ActionChains(driver)

    # * send keys but with the shift keys
    actions\
        .key_down(Keys.SHIFT)\
        .send_keys_to_element(first_name,"abcd")\
        .key_up(Keys.SHIFT)\
        .perform()

    time.sleep(5)
