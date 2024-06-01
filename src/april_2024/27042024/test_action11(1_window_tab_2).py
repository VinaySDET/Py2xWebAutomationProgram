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

    # * open the page
    url="https://the-internet.herokuapp.com/windows"
    driver.get(url)
    driver.maximize_window()

    # * store the handle of the current window
    parent_window=driver.current_window_handle
    print(parent_window)
    time.sleep(3)

    # * find the "click here" link
    link=driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()
    time.sleep(2)

    window_handles=driver.window_handles
    print(window_handles)
    time.sleep(2)
    driver.close()

