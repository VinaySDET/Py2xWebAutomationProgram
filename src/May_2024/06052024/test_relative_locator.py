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
    url = "https://awesomeqa.com/practice.html"
    driver.get(url)
    driver.maximize_window()

    # years_of_experience=driver.find_element(By.XPATH,"//span[contains(text(),'Experience')]")
    driver.find_element(locate_with(By.ID, "exp-3").to_right_of({By.XPATH: "//span[contains(text(),'Experience']"})).click()

    time.sleep(5)
    driver.quit()



