import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_start_browser():
    # selenium API - Create session
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()

    # * start a free trial : this is an anchor tag and we can use on both LINK_TEXT and PARTIAL_TEXT
    # < a
    # href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class ="text-link"
    # data-qa="bericafeqo"
    # >
    # Start a free trial
    # < / a >
    #
    # * LINK_TEXT: if we know the full link
    # link = driver.find_element(By.LINK_TEXT, "Start a free trial")
    # link.click()

    # * PARTIAL _TEXT: if we don't know the full link
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Start ")
    link.click()

    # * Sign in using SSO: this is not  an anchor tag, it's a button
    # <
    # button
    # type = "button"
    # class ="btn btn--link btn--primary Td(u)"
    # onclick="login.goToSSOView()"
    # data-qa="dobevozose"
    # >
    # Sign in using SSO
    # < / button >
    #
    # link = driver.find_element(By.LINK_TEXT, "Sign in using SSO")
    # link.click()

    # button_submit_element = driver.find_element(By.NAME, "Sign in using SSO")
    # button_submit_element.click()