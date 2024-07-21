import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def main(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR,
                                      'div.first_block div.form-group.first_class input[type="text"]')
    first_name.send_keys('Ivan')
    last_name = browser.find_element(By.CSS_SELECTOR,
                                     'div.first_block div.form-group.second_class input[type="text"]')
    last_name.send_keys('Olegovich')
    email = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.form-group.third_class input[type="text"]')
    email.send_keys('ivan_olegovich@gmail.com')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(2)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # закрываем браузер после всех манипуляций
    browser.quit()


class TestMain(unittest.TestCase):
    def test_main_link_2(self):
        main("http://suninjuly.github.io/registration1.html")

    def test_main_link_1(self):
        main("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()
