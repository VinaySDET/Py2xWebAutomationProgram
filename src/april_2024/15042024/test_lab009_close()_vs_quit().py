from selenium import webdriver
import time


# * difference between driver.close() and driver.quit():

# * driver.close():
# Definition: it will close only the current browser window or tab
# Effect: leaves the WebDriver session open.
# Usage: typically used at the end of a single test case
# session id! = null, Error - Invalid session id
# 20% times we use this
# steps:
# 1. run the browser in your current file (ex: https://app.vwo.com/)
# 2. open other tab in running browser(ex: www.bing.com)
# 3. you will see, it will close only the current browser(vwo) but other tab is still open(bing)

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    driver.close()
    time.sleep(5)


# * driver.quit():
# Definition: it will close all browser windows or tab and ends the WebDriver session
# Effect: ends the WebDriver session completely
# Usage: typically used at the end of a test suite or test case
# session id == null, Error - Session id is null
# 80% times we use this
# steps:
# 1. run the browser i your current file(ex: https://app.vwo.com/)
# 2. open other tab in running browser(ex: www.bing.com)
# 3. you will see, all browser / tabs is closed (vwo and bing)

def test_open_login1():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    driver.quit()
    time.sleep(2)
