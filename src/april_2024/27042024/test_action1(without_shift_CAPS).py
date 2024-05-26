from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.NAME, "firstname")
    last_name = driver.find_element(By.NAME, "lastname")

    # create an object for Action Chain class
    actions = ActionChains(driver)

    # send key to an Action Chain object without CAPS
    actions.send_keys_to_element(first_name, "Vinay Kumar").perform()

    actions.send_keys_to_element(last_name, "sdet").perform()
    time.sleep(2)
