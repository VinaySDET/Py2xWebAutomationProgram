# * driver.implicitly_wait(5): i am telling to a web driver to wait for all the elements means everyone have to wait.
# * where we use this: we used when we have a website which is very slow, we want every element to be loaded,
# * we're working in lower environment


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://app.vwo.com/")

    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")

    password_ele = driver.find_element(By.ID, "login-password")
    password_ele.send_keys("Wingify@SDET")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    time.sleep(5)

    # * driver.implicitly_wait(5) :
    # 1. webdriver to wait for all the elements for 5 seconds so that every element will come
    # 2. whenever we are working with lower environment (L.E)
    # L.E are like a production, they have limited bandwidth, limited memory & they're only available for QA testing.

    # * time.sleep(5) :
    # 1. telling to python interpreter to wait for 5 seconds
