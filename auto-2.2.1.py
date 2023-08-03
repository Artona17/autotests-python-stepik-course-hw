from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def sum_two(x, y):
    return str(x+y)


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = int(browser.find_element(By.ID, "num1").text)
    y_value = int(browser.find_element(By.ID, "num2").text)
    sum_two_result = sum_two(x_value, y_value)
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, "[value='" + sum_two_result + "']").click()
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
