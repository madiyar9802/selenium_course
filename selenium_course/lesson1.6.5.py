import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
lesson_link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(lesson_link)
    text = '224592'
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()

    value1 = "input"
    value2 = "last_name"
    value3 = "form-control.city"

    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()