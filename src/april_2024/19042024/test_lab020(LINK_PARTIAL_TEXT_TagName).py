import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # driver.maximize_window()

    # * Make Appointment: this is an anchor tag and we can use on both LINK_TEXT and PARTIAL_TEXT
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg" >
    # Make Appointment
    # < / a >
    #
    # * LINK_TEXT: if we know the full link
    # link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # link.click()
    # time.sleep(2)

    # * PARTIAL _TEXT: if we don't know the full link
    # link = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment ")
    # link.click()
    # time.sleep(2)

    # * By TagName:
    list_of_a_tags= driver.find_elements(By.TAG_NAME, "a")
    make_appointment = list_of_a_tags[5]
    make_appointment.click()
    time.sleep(2)
