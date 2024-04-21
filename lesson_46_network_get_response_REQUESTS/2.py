import requests
import re
from collections import Counter


def find_common_words(urls_list):
    text = ''
    for url in urls_list:
        response = requests.get("https://" + url)
        text += response.text
    words = re.findall(r"\b[a-zA-Z]+\b", text)
    for key, val in Counter(words).most_common(a):
        print(f"{key}, {val}")


a = int(input("Enter top num of key interested: "))
url_list = ["google.com", "facebook.com"]
find_common_words(url_list)

