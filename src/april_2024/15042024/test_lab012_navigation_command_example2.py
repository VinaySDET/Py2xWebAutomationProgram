# * navigation commands in selenium: navigate command are not present in python, but we have only these commands
# 1. refresh
# 2. back

from selenium import webdriver
import time


def test_open_login():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("https://www.bing.com/")
    time.sleep(2)
    driver.back()
    driver.get("https://app.vwo.com/")
    print(driver.title)
    time.sleep(2)
    driver.back()
    print(driver.title)
    time.sleep(2)
    driver.forward()
    print(driver.title)
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    driver.quit()