# * using selenium 3 and selenium 4 :
# * 1. selenium 3: we use to give a selenium browser driver.
# * 2. selenium 4: directly we can use webdriver.Chrome() and no need to set up a driver path.


# * selenium 4:

from selenium import webdriver


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://codewithshani.com/index.php/python-projects/")

    # * python interpreter - optimize if there's no command, it will stop the execution

    driver.quit()
