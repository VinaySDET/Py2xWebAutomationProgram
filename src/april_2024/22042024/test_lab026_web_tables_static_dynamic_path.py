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
    drive = webdriver.Chrome()
    drive.get("https://awesomeqa.com/webtable.html")
    drive.maximize_window()

    # * How to find out the total rows, we have
    row_elements = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print('\n',row)

    # * How to find out the total columns, we have
    col_elements = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)
    time.sleep(2)

    # * i want to get specifically "Giovanni Rovellil" company_name & country_name: //table[contains(@id,'cust')]/tbody/tr[7]/td[3]]
    # specific_detail = drive.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[7]/td[3]")
    # print(f"Total cells: {len(col_elements)}")
    # time.sleep(2)

    # // table[contains( @ id, 'cust')] / tbody / tr                        --> this part is static, because it doesn't change
    # 7-i  --> rows from i: 2,3,4,5,6,7    --> this is dynamic part, because it changes
    # ]/td[                                                                                                  --> this part is static, because it doesn't change
    # 3-j --> rows from j: 1,2,3                --> this is dynamic part, because it changes
    # ]                                                                                                          --> this part is static, because it doesn't change

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):  # range(1,10) -> 1,9+1
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            print(dynamic_path)
            data = drive.find_element(By.XPATH, dynamic_path)
            print(data.text, end=" ")
            print("\n")

    # * Find the Helen Bennett ,where she belongs to(her country) and where she works and her ancestor?
    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = drive.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = drive.find_element(By.XPATH, country_path).text
                print(f"Helen Bennett lives in this country: {country_text}")

                company_path = f"{dynamic_path}/preceding-sibling::td"
                company_text = drive.find_element(By.XPATH, company_path).text
                print(f"Helen Bennett works in this company:{company_text}")

