from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

directory = "/Users/morera/environments/selenium_env/selenium_course/samples/"
file_name = "text.txt"
file_path = os.path.join(directory, file_name)

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.click()
    input1.send_keys("Alex")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.click()
    input2.send_keys("Mo")

    input3 = browser.find_element(By.NAME, "email")
    input3.click()
    input3.send_keys("test@test.com")

    button = browser.find_element(By.ID, "file")
    button.send_keys(file_path)

    subbutton = browser.find_element(By.CLASS_NAME, "btn-primary")
    subbutton.click()


finally:
    time.sleep(10)
    browser.quit()


