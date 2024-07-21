# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
# sleep(5)
#
# # закрываем браузер после всех манипуляций
# browser.quit()
#
#
#
import requests
import bs4 as bs

# Отправляем запрос и получаем HTML-код страницы
url = 'https://www.technodom.kz/catalog/smartfony-i-gadzhety/smartfony-i-telefony/smartfony/f/brands/xiaomi'
page = requests.get(url).text

# Создаем объект BeautifulSoup для парсинга HTML-кода
soup = bs.BeautifulSoup(page, 'html.parser')

# Пример: Найдем все заголовки продуктов (или другие элементы, которые вас интересуют)
product_titles = soup.find_all('p', {'data-testid': 'product-title'})
product_prices = soup.find_all('p', {'data-testid': 'product-price'})

# Печатаем заголовки продуктов
for title in range(len(product_titles)):
    print(product_titles[title].text, '---', product_prices[title].text)
