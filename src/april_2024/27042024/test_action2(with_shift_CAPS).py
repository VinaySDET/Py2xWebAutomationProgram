from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    # last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
    #first_name = driver.find_element(By.NAME, "firstname")
    #last_name = driver.find_element(By.NAME, "lastname")

    #  create an object for Action Chain class with CAPS
    actions = ActionChains(driver)

    # send key to an Action Chain object but with CAPS: {shift down + perform operation + shift up}
    actions \
        .key_down(Keys.SHIFT) \
        .send_keys_to_element(first_name, "vinay") \
        .key_up(Keys.SHIFT).perform()

    # actions = ActionChains(driver)
    # actions \
    #     .key_down(Keys.SHIFT) \
    #     .send_keys_to_element(last_name, "sdet") \
    #     .key_up(Keys.SHIFT).perform()
    # time.sleep(5)
