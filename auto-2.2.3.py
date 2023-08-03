from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Art")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Ona")
    last_name = browser.find_element(By.NAME, "email")
    last_name.send_keys("On@gmail.com")
    file_button = browser.find_element(By.NAME, "file")
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
        path = os.getcwd() + '/' + file.name
        file_button.send_keys(path)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
    os.remove(path)