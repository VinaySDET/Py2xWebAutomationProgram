from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    click_n_hold = driver.find_element(By.ID, "click")
    ActionChains(driver) \
        .click_and_hold(click_n_hold)\
        .perform()

    #assert "resultPage.html" in driver.current_url

    time.sleep(2)
    driver.quit()

    # * click - in click, a normal driver will find the element and click on it, and release it
    # * click_and_hold -> first click and hold, but we will not release it.
    # * action_builder: used for mouse button means you can go back

