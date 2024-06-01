# Logging means - you can add logs to the failure, information, Error.
# Logging means - capture details, which are useful while debugging and show the details about execution of program.
# Warning to the user.
# Information to the user.
# Errors, critical errors to the user.

from selenium import webdriver
import time
import pytest
import allure
import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    logging.basicConfig(filename='test_execution.log', level=logging.INFO)
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    # * Intentional Logging to User
    logging.info("Opened app.vwo website")
    time.sleep(5)  # Simulating a longer test execution
    logging.info("Test execution completed after 5 seconds")
    LOGGER.info(driver.title)
    LOGGER.warning("Test warning")
    LOGGER.error("Test error")
    LOGGER.critical("Test critical error")
    driver.quit()
