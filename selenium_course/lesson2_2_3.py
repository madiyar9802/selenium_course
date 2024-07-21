from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

link1 = "https://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    num1 = browser.find_element(By.CSS_SELECTOR, "span.nowrap#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "span.nowrap#num2").text

    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_visible_text(str(int(num1) + int(num2)))

    button_to_click = browser.find_element(By.TAG_NAME, 'button')
    print(button_to_click.text)
    button_to_click.click()
    sleep(4)

finally:
    if browser:
        browser.quit()
