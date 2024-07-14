import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser.get(link)
    image = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = image.get_attribute("valuex")
    print(type(x))
    calculated_num = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calculated_num)

    not_robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    not_robot_checkbox.click()

    robot_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robot_rule_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit'].btn.btn-default")
    submit_button.click()

    sleep(10)

finally:
    browser.quit()
