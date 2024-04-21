# Напишите функцию extract_emails(text),
# которая извлекает все адреса электронной почты из заданного текста и возвращает
# их в виде списка.
#
# Пример использования:
#
# text = "Contact us at info@example.com or support@example.com for assistance."
#
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']


import re


def extract_emails(txt):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    e_mail = re.findall(pattern, txt)

    return e_mail


text = "Contact us at info@example.com or support@example.com for assistance."
emails = extract_emails(text)
print(emails)



