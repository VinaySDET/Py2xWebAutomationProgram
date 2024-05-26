from telnetlib import EC

from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_action():
    driver = webdriver.Chrome()
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)
    driver.maximize_window()

    # button = driver.find_element(By.XPATH, "// button[@onclick = 'jsAlert()']")
    # button.click()

    # link1 = driver.find_element(By.XPATH, "// button[contains(text(), 'Confirm')]")
    # link1.click()

    button = driver.find_element(By.XPATH, "// button[@onclick = 'jsPrompt()']")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(2)
    alert.send_keys("Hello Vinay")
    time.sleep(5)
    alert.accept()
    # alert.dismiss()

    result = driver.find_element(By.XPATH, "//p[@ id='result']")
    # result = driver.find_element(By.ID,  "result")    ---> you this or above, both are same
    print(result.text)
    assert "Hello Vinay" in result.text
