from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #driver.find_element(By.ID, "click")

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver) \
        .double_click(clickable)\
        .perform()
    time.sleep(5)


