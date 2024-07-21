import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from time import sleep

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    calculation_result_box = browser.find_element(By.ID, 'answer')
    calculation_result_box.send_keys(calc(x))

    solve_button = browser.find_element(By.ID, 'solve')
    solve_button.click()
    sleep(7)

finally:
    browser.quit()
