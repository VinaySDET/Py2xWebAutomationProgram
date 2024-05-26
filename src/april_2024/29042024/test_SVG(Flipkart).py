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
def test_flipkart_search():
    logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    # < div
    # dir = "auto"
    # class ="css-1rynq56 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-13awgt0 r-1bo5ta7 r-1dv474o r-1enofrn" >
    # Search for Products, Brands and More
    # < / div >

    # search_input = driver.find_element(By.
    search_input = driver.find_element(By.NAME,"css-1rynq56 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-13awgt0 r-1bo5ta7 r-1dv474o r-1enofrn")
    # search_input = driver.find_element(By.TAG_NAME,"//div[text()='Search for Products, Brands and More']")
    search_input.send_keys("AC")

    svg_list = driver.find_element(By.XPATH, "//*[local-name()='svg']/*[contains(text(),'Search')]")
    svg_list.click()

    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type="AttachmentType. PNG")
    time.sleep(5)

    driver.quit()
