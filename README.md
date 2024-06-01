### PYTHON WEB AUTOMATION PROGRAMS

### Dependencies we need:

'1. pip install selenium

'2. pip install pytest pytest-html selenium python-xdist allure-pytest openpyxl

'3. pip install pytest pytest-html selenium allure-pytest openpyxl

'4. pytest src/april_2024/12042024/test_lab001.py -s -v

'5. pytest src/april_2024/12042024/test_lab001.py --alluredir=allure-results

'6. allure serve allure-results

'7. allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
