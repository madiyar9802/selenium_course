import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text

    result = calc(x)

    answer_box = browser.find_element(By.ID, "answer")
    answer_box.send_keys(result)

    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_rule_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule_radio)
    robot_rule_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    sleep(5)

finally:
    browser.quit()
