import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.positive
@allure.title("Verify that login is working in CURA HEALTH Website")
@allure.description("TC#1 Simple Login check on CURA katalone website.")
def test_india_map():
    logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()

    states = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break
    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type="AttachmentType. PNG")

    driver.quit()
