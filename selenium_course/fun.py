from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'https://www.technodom.kz/'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Пропускаем выбор города
    city_choose_button = browser.find_element(By.CSS_SELECTOR,
                                              '.ModalNext__CloseBtn.ModalNext__CloseBtn-Cross.reset-button-styles')
    city_choose_button.click()

    # Переходим по ссылке: "каталог"
    catalog = browser.find_element(By.CSS_SELECTOR, '[href="/catalog"]')
    catalog_link = catalog.get_attribute('href')
    browser.get(catalog_link)

    # Парсим данные по всем ссылкам каталога (Смартфоны и гаджеты, Ноутбуки и компьютеры и т.д.)
    parse_product = browser.find_elements(By.CSS_SELECTOR, 'a[class*="CatalogPage_link"]')
    parse_product_links = [x.get_attribute('href') for x in parse_product]


    # Для теста парсим данные по одной ссылке
    # browser.get(parse_product_links[0])

    def parse_by_link(link):
        browser.get(link)
        products = browser.find_elements(By.CSS_SELECTOR, 'p[data-testid="product-title"]')
        prices = browser.find_elements(By.CSS_SELECTOR, 'p[data-testid="product-price"]')
        product_and_prices = []
        for i in range(len(products)):
            product_and_prices.append([products[i].text, prices[i].text])

        print(product_and_prices)
        print()
        print('*' * 50)
        print()
        print()


    for i in range(5):
        parse_by_link(parse_product_links[i])

    sleep(5)

finally:
    browser.quit()
