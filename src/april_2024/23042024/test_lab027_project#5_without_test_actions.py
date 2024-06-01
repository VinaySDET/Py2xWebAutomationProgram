from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import allure
from selenium.webdriver.support.select import Select


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.send_keys("Vinay")
    time.sleep(2)

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("Kumar")
    time.sleep(2)

    gender=driver.find_element(By.XPATH,"//input[@id='sex-0']")
    gender.click()
    time.sleep(2)

    year_of_exp = driver.find_element(By.XPATH, "//input[@id='exp-2']")
    year_of_exp.click()
    time.sleep(2)

    date = driver.find_element(By.XPATH, "//input[@id='datepicker']")
    date.send_keys("30-05-2024")
    time.sleep(2)

    profession= driver.find_element(By.XPATH, "//input[@id='profession-1']")
    profession.click()
    time.sleep(2)

    dropdown_continents = Select(driver.find_element(By.XPATH, "//select[@id='continents']"))
    dropdown_continents.select_by_visible_text("Europe")
    time.sleep(2)

    dropdown_selenium_commands = Select(driver.find_element(By.XPATH, "//select[@id='selenium_commands']"))
    dropdown_selenium_commands.select_by_visible_text("Navigation Commands")
    time.sleep(2)

    # upload_img = driver.find_element(By.XPATH, "//input[@id='photo']")
    # upload_img.click()
    # time.sleep(2)

    download_file = driver.find_element(By.XPATH, "//a[contains(text(),'Click here to')]")
    download_file.click()
    time.sleep(2)
    driver.close()

    submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    submit_button.click()
    time.sleep(2)






