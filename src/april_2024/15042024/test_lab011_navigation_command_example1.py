from selenium import webdriver
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")
    time.sleep(2)
    driver.forward()

    driver.get("https://www.youtube.com/?bp=wgUCEAE%3D")
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)

# * Navigation commands in selenium
# get(String url): this command is used to open a specific URL in the browser
# driver.get("http://www.example.com/")
# navigate().to(String url) -Not Exist in python












