from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    magical_journey_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')
    magical_journey_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    x = calc(x)

    answer_block = browser.find_element(By.ID, 'answer')
    answer_block.send_keys(x)

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')
    submit_button.click()
    sleep(10)

finally:
    browser.quit()
