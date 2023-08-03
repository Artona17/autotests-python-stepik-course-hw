from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input_calc = browser.find_element(By.ID, "answer")
    input_calc.send_keys(y)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    robot_radiobutton.click()
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
