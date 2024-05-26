# use this website link: https://katalon-demo-cura.herokuapp.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

# * Find the element of the anchor tag and click on button
# <a
# id="btn-make-appointment"
# href="./profile.php#login"
# class="btn btn-dark btn-lg"
# >
# Make Appointment
# </a>
    log_in_ele = driver.find_element(By.ID, "btn-make-appointment")
    log_in_ele.click()
    time.sleep(10)
    assert driver.title == "CURA Healthcare Service"
    driver.quit()
    print("Test Passed")