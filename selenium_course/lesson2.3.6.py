from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


link = 'https://suninjuly.github.io/redirect_accept.html'

try:
    b = webdriver.Chrome()
    b.get(link)

    magical_journey_button = b.find_element(By.CSS_SELECTOR, 'button[type="submit"].trollface.btn.btn-primary')
    magical_journey_button.click()

    new_window = b.window_handles[1]
    b.switch_to.window(new_window)

    x = b.find_element(By.ID, 'input_value').text
    x = calc(x)

    answer = b.find_element(By.ID, 'answer')
    answer.send_keys(x)

    submit_button = b.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')
    submit_button.click()
    sleep(7)

finally:
    b.quit()
