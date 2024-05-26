# selenium- it helps you to Automates the Browser
# selenium 3 - 20% on the selenium 3 - JSON write protocol(API requests)
# selenium 4 - 70% + (migrated to selenium 4) , w3c protocol. selenium manager
# * selenium manager: Definition
# 1. when you install pip install selenium and
# 2. the version is greater than 4.x then you don't have to set up the browser drivers.

# * In selenium 3 code - we use to give selenium driver browser

from selenium import webdriver

driver_path = "D:/computer-softwares/edgedriver_win64/msedgedriver.exe"
driver = webdriver.EdgeService(executable_path=driver_path)
driver.get("https://codewithshani.com/index.php/python-projects/")
