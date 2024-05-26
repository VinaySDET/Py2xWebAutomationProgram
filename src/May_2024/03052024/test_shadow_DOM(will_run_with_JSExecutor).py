from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shadow_DOM():
    driver = webdriver.Chrome()
    url = "https://selectorshub.com/xpath-practice-page/"
    driver.get(url)
    driver.maximize_window()

    username=driver.find_element(By.XPATH,"//div[@class='jackPart']")
    js_executor=driver.execute_script
    js_executor("arguments[0].scrollIntoView(true);",username)
    #username.send_keys("vinay kumar")
    time.sleep(2)

    pizza=driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
    pizza.send_keys("Golden Corn")
    time.sleep(2)

    # pizza = driver.find_element(By.ID, "'pizza")
    # js_exec = driver.execute_script
    # js_exec("arguments[0].click();", pizza)
    # # pizza.send_keys("Golden Corn")
