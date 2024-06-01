from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID,"clickable")
    actions = ActionChains(driver)
    actions\
        .click_and_hold(clickable)\
        .key_down(Keys.SHIFT)\
        .send_keys("vinay-sdet")\
        .key_up(Keys.SHIFT)\
        .perform()
    # actions.click_and_hold(clickable).key_down(Keys.SHIFT).key_down("vinay").perform()

    time.sleep(2)
    driver.quit()

    # click - normal
    # click_and_hold -> will not release

