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

    go_next_and_go_back=driver.find_element(By.ID, "click")
    go_next_and_go_back.click()

    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_up(MouseButton.BACK)
    time.sleep(2)
    # actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.perform()

    time.sleep(2)

# * action_builder: used for mouse pointer events and mouse clicking button but maximum time we will use action chains.
# * Navigating to a page ,click on release and moving back to previous page.