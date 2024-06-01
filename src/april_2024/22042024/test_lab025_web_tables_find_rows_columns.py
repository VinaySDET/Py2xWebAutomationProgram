from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

def test_web_tables():
    drive = webdriver.Chrome()
    drive.get("https://awesomeqa.com/webtable.html")
    drive.maximize_window()

    # * How to read and get all the values/elements from the table.
    read_all_elements = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]")
    row = len(read_all_elements)
    print("\n")
    print(f"read all the values:", row)
    time.sleep(2)

    # * How to find out the single row
    row_elements = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]")
    row = len(row_elements)
    print(f"single row:", row)
    time.sleep(2)

    # * How to find out the total rows
    row_elements = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(f"Total rows", row)
    time.sleep(2)

    # * How to find out the single column
    col_elements = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td[1]")
    col = len(col_elements)
    print(f"single column :", col)
    time.sleep(2)

    # * How to find out the total columns
    col_elements = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(f"Total columns in a table is:", col)
    time.sleep(2)

    # * i want to get specifically "Roland Mendel" name: //td[contains(text(),'Roland')]
    specific_detail = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[4]/td[2]")
    roland_len=len(specific_detail)
    print(f"Total Roland element in a table is: ",specific_detail)
    #print(f"Total Roland element in a table is: {len(specific_detail)}")
    time.sleep(2)

