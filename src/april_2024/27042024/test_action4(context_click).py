from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")

    actions = ActionChains(driver)

    # send key to an Action Chain object but with CAPS: {shift down + perform operation + shift up}
    actions \
        .key_down(Keys.SHIFT) \
        .send_keys_to_element(first_name, "vinay-sdet") \
        .key_up(Keys.SHIFT).context_click().perform()
    time.sleep(2)



