from selenium import webdriver
import time
import pytest
import allure


@pytest.mark.smoke
@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password Fails"
                    " if any error happens, Note that this test does not test 2-Factor Authentication.")

def test_open_login():
    driver = webdriver.Chrome()  # POST request - creates the session
    driver.get("https://codewithshani.com/index.php/python-projects/")  # GET request - url parameters
    print(driver.title)
    assert driver.title == "Python Projects – CodeWithShani"
    time.sleep(2)
    # driver.quit()

    # * assertion: you can use assertion with using import pytest and @pytest.mark.normal