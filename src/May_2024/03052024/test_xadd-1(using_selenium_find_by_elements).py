from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_element():
    driver = webdriver.Chrome()
    url = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(url)
    driver.maximize_window()

    add_element=driver.find_element(By.XPATH,"//button[@onclick='addElement()']")
    add_element.click()

    time.sleep(2)