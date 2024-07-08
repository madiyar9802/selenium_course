from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

search_text = input("Введите поисковую фразу: ")
try:
    browser = webdriver.Chrome()
    browser.get("https://www.google.kz/")
    search_line = browser.find_element(By.CSS_SELECTOR, "textarea[aria-label]")
    search_line.send_keys(search_text)
    button = browser.find_element(By.XPATH, '//div[4]/center/input[1]')
    button.click()
    sleep(1)
    secure_links = browser.find_elements(By.CSS_SELECTOR, 'a[href^="https"]')
    for link in secure_links[10::]:
        print(link.get_attribute('href'))

finally:
    browser.quit()
