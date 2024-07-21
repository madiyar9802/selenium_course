import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "div.form-group span.nowrap#input_value")
    x = x_element.text
    y = calc(x)

    answer_block = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_block.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR,
                                    "div.form-check.form-check-custom label.form-check-label[for='robotCheckbox']"
                                    )
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR,
                                 "div.form-check.form-radio-custom input.form-check-input[value='robots']"
                                 )

    radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit'].btn.btn-default")
    submit_button.click()
    sleep(5)
finally:
    browser.quit()
