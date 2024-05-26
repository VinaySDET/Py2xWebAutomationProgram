from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    clickable = driver.find_element(By.ID, "click")
    ActionChains(driver) \
        .click(clickable)\
        .perform()

    #assert "resultPage.html" in driver.current_url

    time.sleep(2)
    driver.quit()

    # click - in normal click action will perform
    # click_and_hold -> we will click, but we will not release
    # action_builder: used for mouse button

