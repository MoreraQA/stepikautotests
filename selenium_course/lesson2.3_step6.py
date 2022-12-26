from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, "trollface")
    button1.click()

    new_tab = browser.window_handles[1]

    browser.switch_to.window(new_tab)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    res = calc(x)

    field = browser.find_element(By.ID, "answer")
    field.click()
    field.send_keys(res)

    confirm = browser.find_element(By.CLASS_NAME, "btn-primary")
    confirm.click()

finally:
    time.sleep(10)
    browser.quit()