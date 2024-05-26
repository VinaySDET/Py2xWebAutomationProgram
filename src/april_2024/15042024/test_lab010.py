from selenium import webdriver
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    time.sleep(2)
    driver.get("https://www.youtube.com/?bp=wgUCEAE%3D")
    driver.maximize_window()
    time.sleep(2)
    print(driver.title)   # Title is : YouTube

# * time.sleep(5) :
# means we're telling to python interpreter that to wait for 5 seconds before we move to the next command
# we're not telling to the webDriver
