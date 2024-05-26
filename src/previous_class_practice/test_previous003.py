# 1. Open the browser
# 2. Navigate to a URL
# 3. Find the email WebElement and put email id = "abc@gmail.com"
# 4. Find the password input box and enter the password = 123
# 5. Click on the button - sign in
# 6. Verify that the dashboard is loaded - pytest
# 7. create a report to send to QA Lead - HTML -> Allure Report

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open the browser
    # navigate to URL-- navigation commands in selenium
    # get(string_url - this command is used to open a specific URL in the browser)... example: driver.get("https://example.com")
    driver.get("https://codewithshani.com/index.php/python-projects/")

    # # * username
    # # < input
    # # dir = "ltr"
    # # id = ":rn:"
    # # class ="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"
    # # type="text"
    # # value name="email"
    # # fdprocessedid="qs4zk"
    # # >
    #
    # # * password
    # # < input
    # # dir = "ltr"
    # # id = ":rq:"
    # # class ="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"
    # # type="password"
    # # value=""
    # # name="pass"
    # # fdprocessedid="c3782o"
    # # >
    email_address_ele=driver.find_element(By.ID, ":rn:")
    password_ele=driver.find_element(By.NAME, ":rq:")
    log_in_ele = driver.find_element(By.ID, "loginbutton")
    #
    # # sending the data -? email & password -> clicking on the button
    # # sendkeys and click()
    email_address_ele.send_keys("bloggerjohn3@gmail.com")
    password_ele.send_keys("Vinay@blogger")
    log_in_ele.click()
    time.sleep(10)
