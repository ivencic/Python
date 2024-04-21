"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и
уровень заголовков, а затем использует библиотеку Beautiful Soup для парсинга HTML и
извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
"""

import requests
from bs4 import BeautifulSoup


def get_headers(web_page, h_level):
    html = requests.get("https://" + web_page).text
    soup = BeautifulSoup(html, "html.parser")
    headers = soup.find_all("h" + h_level)
    for i in headers:
        print(i)


url = input("Введите адрес страницы: ")
h_lvl = input("Введите уровень заголовка: ")
get_headers(url, h_lvl)
