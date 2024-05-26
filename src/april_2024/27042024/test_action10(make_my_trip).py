from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


def test_action():
    driver = webdriver.Chrome()
    url = "https://www.makemytrip.com/"
    driver.get(url)
    driver.maximize_window()

    fromCity = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).send_keys("Goa").perform()

    # fromCity = driver.find_element(By.ID, "fromCity")
    # actions=ActionChains(driver).move_to_element(fromCity).click().send_keys("Kerala").perform()

    time.sleep(2)

# * Task:
# 1. Find the element
# 2. move to the element in search box
# 3. perform send keys
