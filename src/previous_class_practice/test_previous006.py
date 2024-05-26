# Logging means - you can add logs to the failure, information, Error
# Logging means - capture details, which are useful while debugging and show the details about execution of program
# warning to the user
# information to the user
# Errors, critical errors to the user

import logging


def test_print_logs():
    logger = logging.getLogger(__name__)
    # intentionally logging to user
    logger.info("This is Information Logs")
    logger.warning("This is Warning Logs")
    logger.error("This is  Error Logs")
    logger.critical("This is Critical Logs")
