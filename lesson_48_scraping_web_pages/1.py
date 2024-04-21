"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок
на странице.

"""


import requests
from bs4 import BeautifulSoup


def get_site_links(url):
    all_html = requests.get("https://" + url).text
    soup = BeautifulSoup(all_html, "html.parser")
    links = soup.find_all("a")
    for item in links:
        print(item["href"])


address = input("Введите адрес страницы: ")
get_site_links(address)
