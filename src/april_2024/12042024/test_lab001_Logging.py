# Logging means - you can add logs to the failure, information, Error
# Logging means - capture details, which are useful while debugging and show the details about execution of program
# warning to the user
# information to the user
# Errors, critical errors to the user

from selenium import webdriver
import time
import pytest
import allure
import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://codewithshani.com/index.php/python-projects/")

    # * Intentional Logging to User
    LOGGER.info("This is information logs")
    LOGGER.info(driver.title)
    LOGGER.warning("Test warning")
    LOGGER.error("Test error")
    LOGGER.critical("Test critical error")
