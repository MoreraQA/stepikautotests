from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "book")

    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    res = calc(x)

    field = browser.find_element(By.ID, "answer")
    field.click()
    field.send_keys(res)

    confirm = browser.find_element(By.ID, "solve")
    confirm.click()

finally:
    time.sleep(10)
    browser.quit()