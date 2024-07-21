import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'http://suninjuly.github.io/file_input.html'

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(current_dir)
file_path = os.path.join(parent_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, 'input[type="text"][name="firstname"].form-control')
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[type="text"][name="lastname"].form-control')
    email = browser.find_element(By.CSS_SELECTOR, 'input[type="text"][name="email"].form-control')
    file = browser.find_element(By.ID, 'file')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    first_name.send_keys('Test')
    last_name.send_keys('Testov')
    email.send_keys('testovich@qwerty.com')
    file.send_keys(file_path)
    submit_button.click()
    sleep(5)

finally:
    browser.quit()
