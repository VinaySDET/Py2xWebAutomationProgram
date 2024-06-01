from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.select import Select


def test_action():
    driver = webdriver.Chrome()
    url = "https://www.makemytrip.com/"
    driver.get(url)
    driver.maximize_window()

    fromCity = driver.find_element(By.XPATH,"//input[@id='fromCity']")
    fromCity.send_keys("Bengaluru")

    # dropdown_continents = Select(driver.find_element(By.XPATH, "//select[@id='continents']"))
    # dropdown_continents.select_by_visible_text("Europe")
    # time.sleep(2)

    # actions = ActionChains(driver)
    # actions.move_to_element(fromCity).send_keys("Bengaluru").perform()
    #
    # # fromCity = driver.find_element(By.ID, "fromCity")
    # # actions=ActionChains(driver).move_to_element(fromCity).click().send_keys("Kerala").perform()

    time.sleep(10)

# * Task:
# 1. Find element
# 2. Move to the element in search box
# 3. Perform send keys
