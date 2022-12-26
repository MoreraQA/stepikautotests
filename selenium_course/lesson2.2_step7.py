from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text

    res = calc(x)

    field1 = browser.find_element(By.ID, "answer")
    field1.click()
    field1.send_keys(res)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    submits = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submits)
    submits.click()


finally:
    time.sleep(10)
    browser.quit()
