from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium import webdriver
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with


def test_relative_locator():
    driver = webdriver.Chrome()
    url = "https://www.aqi.in/real-time-most-polluted-city-ranking"
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)

    # *use anyone either XPATH or direct normal path
    #search_city=driver.find_element(By.XPATH,"//input[@id='search_city']")
    search_city = driver.find_element(By.ID,"search_city")
    search_city.send_keys("India")
    time.sleep(5)

    list_of_states = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")
    print("\n","Name" +  " | "  +  "ACQ"  +  " | "  +  "Rank" )
    for state in list_of_states:
        if "India" in state.text:
            s1 = driver.find_element(locate_with(By.TAG_NAME, "p").to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(state)).text
            s3 = driver.find_element(locate_with(By.TAG_NAME, "p").above(state)).text
            s4 = driver.find_element(locate_with(By.TAG_NAME, "p").below(state)).text
            print(state.text + " | " + s1 + " | " + s2)
            print(state.text + " | " + s3 + " | " + s4)





