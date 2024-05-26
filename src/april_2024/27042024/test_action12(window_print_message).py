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
    url="https://the-internet.herokuapp.com/windows"
    driver.get(url)
    driver.maximize_window()

    parent_window=driver.current_window_handle
    print(parent_window)

    link=driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()

    window_handles=driver.window_handles
    print(window_handles)
    time.sleep(2)

    # * Example-1: show the title of the new window
    for handle in window_handles:
        driver.switch_to.window(handle)
        if handle!=parent_window:
            print(driver.title)
            time.sleep(2)
            break
    driver.switch_to.window(parent_window)
    time.sleep(2)
    #  * OUTPUT: New Window

    # * Example-2: print the message
    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print ("Test case passed, switched to a child window")
            break
    driver.switch_to.window(parent_window)
    time.sleep(2)
    # * OUTPUT: Test case passed, switched to a child window
