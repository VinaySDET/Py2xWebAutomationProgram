# * selenium 4


from selenium import webdriver
import time
import pytest


def test_open_login():
    driver = webdriver.Chrome()  # POST request - creates the session
    driver.get("https://codewithshani.com/index.php/python-projects/")  # GET request - url parameters
    print(driver.title)
    time.sleep(5)
    driver.quit()

# * time.sleep(5) :
# means we're telling to python interpreter that wait for 5 seconds before we move to the next command
# we're not telling to the webDriver

# * driver.title: Return the title of the current page i.e., Python Projects – CodeWithShani