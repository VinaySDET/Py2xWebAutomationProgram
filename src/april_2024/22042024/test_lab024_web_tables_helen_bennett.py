from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure


@pytest.mark.smoke
@allure.title("Verify that login to IDrive 360 is working fine")
@allure.description("TC #1 - Simple Login Check on Idrive 360 Website")
def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()
    time.sleep(2)

    # * Helen Bennett: //td[text()='Helen Bennett'] or  //td[contains(text(),'Helen')]
    # * Helen preceding sibling: //td[text()='Helen Bennett']/preceding-sibling::td  or  //td[contains(text(),'Helen')]/preceding-sibling::td
    # * Helen following sibling: //td[text()='Helen Bennett']/following-sibling::td   or //td[contains(text(),'Helen')]/following-sibling::td

    # * Helen Bennett:
    user=driver.find_element(By.XPATH,"//td[contains(text(),'Helen')]")
    print(user)
    time.sleep(2)

    # * Helen preceding sibling:
    user = driver.find_element(By.XPATH, "//td[contains(text(),'Helen')]/preceding-sibling::td")
    # user.click()
    time.sleep(2)

    # * Helen following sibling:
    user = driver.find_element(By.XPATH, "//td[contains(text(),'Helen')]/following-sibling::td")
    # user.click()
    time.sleep(2)

    # * How to find out the total rows
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    # * How to find out the total cells
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)
    time.sleep(2)
