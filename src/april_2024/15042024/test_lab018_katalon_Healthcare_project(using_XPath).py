# * Selenium Project - #1 - Test Case to Automate [Mini Project]
# * page-1:
# open the url - https://katalon-demo-cura.herokuapp.com/
# click on the make appointment button
# verify that url changes - assert
# * page-2:
# enter the username, password and click login
# * page-3:
# select 2nd option in facility
# select checkbox
# select any radio box option in Healthcare program
# enter the date
# write anything on comment section
# click on Book Appointment
# * finally:
# verify that the Appointment Confirmation message is visible on the page

import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.negative
def test_katalon_appointment_negative():
    logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(2)

    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link.click()
    time.sleep(2)

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")
    time.sleep(2)

    password = driver.find_element(By.NAME, "password")
    password.send_keys("John Doe")
    time.sleep(2)

    login = driver.find_element(By.ID, "btn-login")
    login.click()
    time.sleep(2)

    # * wrong password:
    # < p class ="lead text-danger" >
    # Login failed! Please ensure the username and password are valid.
    # < / p >

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed! " in error_message.text

    # * wrong URL:


@pytest.mark.positive
@allure.title("Verify that login is working in CURA HEALTH Website")
@allure.description("TC#1 Simple Login check on CURA katalone website.")
def test_katalon_appointment_posistive():
    logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # * verify the change URL - using assert
    curr_url = driver.current_url
    assert curr_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(2)

    # * click on the make appointment button
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg"
    # >
    # Make Appointment
    # < / a >

    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link.click()
    allure.attach(driver.get_screenshot_as_png(),name="screenshot",attachment_type="AttachmentType. PNG")
    print(driver.current_url)


    # * verify the change URL - using assert
    curr_url = driver.current_url
    assert curr_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion- Fail Message #1 - Error matching the URL"

    assert driver.title == "CURA Healthcare Service"
    time.sleep(2)

    # * page-2:
    # enter the username
    # < input
    # type = "text"
    # class ="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value=""
    # autocomplete="off"
    # fdprocessedid="q964nx"
    # >

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")
    time.sleep(2)

    # enter the password:
    # < input
    # type = "password"
    # class ="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"
    # value=""
    # autocomplete="off"
    # fdprocessedid="839cfl"
    # >
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    time.sleep(2)

    # enter the Login:
    # <
    # button id = "btn-login"
    # type = "submit"
    # class ="btn btn-default"
    # fdprocessedid="p9nicl"
    # >
    # Login
    # < / button >
    login = driver.find_element(By.ID, "btn-login")
    login.click()
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type="AttachmentType. PNG")
    time.sleep(2)

    # * verify the change URL - using assert
    curr_url = driver.current_url
    assert curr_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Assertion- Fail Message #2 -Enter wrong URL(Appointment)"

    # * page-3:
    # select 2nd option in facility

    # < select
    # id = "combo_facility"
    # name = "facility"
    # class ="form-control"
    # fdprocessedid="lhcev7" >

    # < option value = "Tokyo CURA Healthcare Center" >
    # Tokyo CURA Healthcare Center
    # < / option >

    # < option value = "Hongkong CURA Healthcare Center" >
    # Hongkong CURA Healthcare Center
    # < / option >

    # < option value = "Seoul CURA Healthcare Center" >
    # Seoul CURA Healthcare Center
    # < / option >
    # < / select >

    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
    time.sleep(2)

    # select radio box, checkbox
    # < label for ="chk_hospotal_readmission"
    # class ="checkbox-inline"
    # >
    # < input type = "checkbox"
    # id = "chk_hospotal_readmission"
    # name = "hospital_readmission"
    # value = "Yes" > Apply for hospital readmission
    # < / label >

    hospital_readmission = driver.find_element(By.ID, "chk_hospotal_readmission")
    hospital_readmission.click()
    time.sleep(2)

    # select Healthcare program
    # < label class ="radio-inline" >
    # < input type = "radio"
    #  name = "programs"
    #  id = "radio_program_medicaid"
    #  value = "Medicaid" >
    #  Medicaid
    #  < / label >

    program_medicaid = driver.find_element(By.ID, "radio_program_medicaid")
    program_medicaid.click()
    time.sleep(2)

    # enter the date and text
    # < label for ="txt_visit_date"
    # class ="col-sm-offset-3 col-sm-2 control-label" >
    # Visit Date (Required)
    # < / label >

    visit_date = driver.find_element(By.ID, "txt_visit_date")
    visit_date.send_keys("19/04/2024")
    time.sleep(2)

    # write something on a comment section:
    # < textarea class ="form-control"
    # id="txt_comment"
    # name="comment"
    # placeholder="Comment"
    # rows="10"
    # data-gramm="false"
    # wt-ignore-input="true" >
    # < / textarea >

    comment = driver.find_element(By.ID, "txt_comment")
    comment.send_keys("I am testing this website using Selenium-Automaton")
    time.sleep(2)

    # clicks on Book Appointment:
    # < button id = "btn-book-appointment"
    # type = "submit"
    # class ="btn btn-default"
    # fdprocessedid="1d9tcd" >
    # Book Appointment
    # < / button >

    book_appointment = driver.find_element(By.ID, "btn-book-appointment")
    book_appointment.click()
    time.sleep(2)

    # * finally:
    # verify that the Appointment Confirmation message is visible on the page:
    # < section id = "summary"
    # class ="section bg-primary" >
    # < div class ="container" >
    # < div class ="row" >
    # < div class ="col-xs-12 text-center" >
    # < h2 > Appointment Confirmation < / h2 >
    # < p class ="lead" >
    # Please be informed that your appointment has been booked as following:
    # < / p >

    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in heading_h2.text
    time.sleep(2)

    assert "CURA Healthcare Service" in driver.title
    assert driver.title == "CURA Healthcare Service"
    time.sleep(2)


    curr_url = driver.current_url
    assert curr_url == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"



    # assert "Dashboard" in driver.title
    # assert driver.title == "Dashboard"

    # logger = logging.getLogger(__name__)
    # logger.info('title is - ' + driver.title)
    #
    # assert "Dashboard" in driver.title
    # assert driver.title == "Dashboard"
