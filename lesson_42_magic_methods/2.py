"""

Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
- Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
- Преобразование письма в строку (метод __str__)
- Получение длины текста письма (метод __len__)
- Получение хеш-значения письма (метод __hash__)
- Проверка наличия текста в письме (метод __bool__)

Пример использования:
email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

print(email1)  # Вывод:

From: john@example.com
To: jane@example.com
Subject: Meeting

Hi Jane, let's have a meeting tomorrow.


print(len(email2))  # Вывод: 24
print(hash(email3))  # Вывод: -920444056
print(bool(email1))  # Вывод: True
print(email2 > email3)  # Вывод: True
"""

import datetime
import functools


@functools.total_ordering
class Email:
    def __init__(self, sender, receiver, title, msg, date):
        self.date = datetime.date(*map(int, date.split("-")))
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.msg = msg

    def __eq__(self, other):
        if self.date == other.date:
            return True
        return False

    def __lt__(self, other):
        if self.date < other.date:
            return True
        return False

    def __str__(self):
        return (f" From: {self.sender}\n To: {self.receiver}\n Title: {self.title}\n"
                f" Text: {self.msg}")

    def __len__(self):
        return len(self.msg)

    def __hash__(self):
        return hash(self.msg) + hash(self.title) + hash(self.sender) + hash(self.date) + hash(self.receiver)

    def __bool__(self):
        if self.msg != "":
            return True
        return False


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.",
               "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

print(email1)
print()
print(len(email2))
print(hash(email3))
print(bool(email1))
print(email2 > email3)
print(email1 < email3)
