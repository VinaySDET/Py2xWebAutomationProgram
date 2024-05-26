import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.positive
@allure.title("Verify that login is working in CURA HEALTH Website")
@allure.description("TC#1 Simple Login check on CURA katalone website.")
def test_i360_posistive():
    logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login/")
    driver.maximize_window()

    # * verify the change URL - using assert
    curr_url = driver.current_url
    assert curr_url == "https://www.idrive360.com/enterprise/login"
    time.sleep(2)

    # < input _ngcontent - yqn - c4 = ""
    # autofocus = ""
    # class ="id-form-ctrl ng-valid ng-touched ng-dirty"
    # id="username"
    # name="username"
    # type="email" >

    username = driver.find_element(By.ID, "username")
    username.send_keys("augtest_040823@idrive.com")
    time.sleep(2)

    # < input_ngcontent - yqn - c4 = ""
    # class ="id-form-ctrl ng-valid ng-dirty ng-touched"
    # id="password"
    # name="password"
    # tabindex="0"
    # type="password" >

    password = driver.find_element(By.ID, "password")
    password.send_keys("123456")
    time.sleep(2)

    # < button_ngcontent - yqn - c4 = ""
    # class ="id-btn id-info-btn-frm"
    # id="frm-btn"
    # type="submit" >
    # Sign in
    # < / button >
    login = driver.find_element(By.ID, "frm-btn")
    login.click()
    # allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type="AttachmentType. PNG")
    time.sleep(5)

    # # * verify the change URL - using assert
    # curr_url = driver.current_url
    # assert curr_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Assertion- Fail Message #2 -Enter wrong URL(Appointment)"

    # < div_ngcontent - xnn - c10 = ""
    # class ="id-card-blk id-expire-msg id-expire-msg-nw failure"
    # id="expiredmsg" >
    # < div _ngcontent-xnn-c10=""
    # class ="id-card-cont" >
    # < i _ngcontent-xnn-c10=""
    # class ="id-expire-msg-icon" >
    # < / i >
    # < h5 _ngcontent-xnn-c10=""
    # class ="id-card-title" >
    # Your free trial has expired
    # < / h5 >
    # < p _ngcontent-xnn-c10="" >
    # and your account has been canceled.
    # < / p >
    # < p _ngcontent-xnn-c10="" >
    # In order to reactivate your account, upgrade your account and save 25 % *.
    # < / p >
    # < / div >
    # < / div >

    # < h5_ngcontent - xnn - c10 = ""
    # class ="id-card-title" >
    # Your free trial has expired
    # < / h5 >

    # heading_h5 = driver.find_element(By.TAG_NAME, "h5")
    # assert "Your free trial has expired" in heading_h5.text

    a=driver.find_element(By.XPATH, "//*[contains(text(),'Your trial has expired')]")
    a.text

    time.sleep(2)
    # assert expiredmsg.text == "Your free trial has expired\nand your account has been canceled.\nIn order to reactivate your account, upgrade your account and save 25 % *.", "Assertion- Fail Message #3 -Enter wrong URL(Appointment)"

    # * verify the change URL - using assert
    # curr_url = driver.current_url
    # assert curr_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Assertion- Fail Message #4 -Enter wrong URL(Appointment)"
    # time.sleep(2)

