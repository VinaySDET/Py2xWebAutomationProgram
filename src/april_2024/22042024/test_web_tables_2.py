from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure


def test_web_tables():
    drive = webdriver.Chrome()
    drive.get("https://awesomeqa.com/webtable1.html")
    drive.maximize_window()

    # * How to read and get all the values/elements from the table.
    table = drive.find_element(By.XPATH, "//table[contains(@summary,'Sample')]/tbody")
    # row_table="//table[contains(@summary,'Sample']/tbody/tr[4]/td[1]"
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        cols=row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            print(e.text)
            if "UAE" in e.text:
                print("YES!, UAE exist in this table")
