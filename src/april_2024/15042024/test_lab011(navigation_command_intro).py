from selenium import webdriver
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.get("https://www.youtube.com/?bp=wgUCEAE%3D")
    driver.maximize_window()
    time.sleep(2)
    print(driver.title)   # Title is: YouTube

# * Navigation commands in selenium
# get(String url): this command is used to open a specific URL in the browser
# driver.get("http://www.example.com/")
# navigate().to(String url) -Not Exist in python

# * navigation commands in selenium: navigate command are not present in python, but we have only these commands
# 1. refresh
# 2. back
# 3. forward
    # driver.get("http://www.example")
    driver.back()
    driver.forward()
    driver.refresh()
