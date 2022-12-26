from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.ID, "num1").text
    second = browser.find_element(By.ID, "num2").text
    result = int(first) + int(second)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()