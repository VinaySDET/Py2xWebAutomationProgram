from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with


def test_relative_locator():
    driver = webdriver.Chrome()
    url = "https://www.google.com/"
    driver.get(url)
    driver.maximize_window()
    try:
        username = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
        driver.refresh()
        username = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
        username.send_keys("sabarimala")
    except StaleElementReferenceException as SEE:
        print( SEE)
    time.sleep(2)


# * how to fix stale Exception: you have to put driver.find element again after driver.refresh() element