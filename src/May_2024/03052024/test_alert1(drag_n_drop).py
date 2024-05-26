from telnetlib import EC

from selenium.webdriver.common import actions
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drag_drop():
    driver = webdriver.Chrome()
    url = "https://the-internet.herokuapp.com/drag_and_drop"
    driver.get(url)
    driver.maximize_window()

    # * drag and drop means, swapped from box a to box b
    draggable = driver.find_element(By.XPATH, "//div[@id='column-a']")
    droppable = driver.find_element(By.XPATH, "//div[@id='column-b']")
    ActionChains(driver).drag_and_drop(draggable, droppable).perform()
    time.sleep(2)

    # * Again, drag and drop means, swapped from box b to box a
    draggable = driver.find_element(By.XPATH, "//div[@id='column-b']")
    droppable = driver.find_element(By.XPATH, "//div[@id='column-a']")
    ActionChains(driver) \
        .click_and_hold(draggable) \
        .move_to_element(droppable) \
        .release(droppable)\
        .perform()
    time.sleep(2)

# * click_and_hold: it's recommended method coz it works with all browsers