"""
    1.
    Напишите программу, которая подсчитывает количество вхождений
    каждого слова в тексте и выводит на экран наиболее часто встречающиеся слова.
    Для решения задачи используйте класс Counter из модуля collections.
    Создайте функцию count_words, которая принимает текст в качестве аргумента и
    возвращает словарь с количеством вхождений каждого слова.
    Выведите наиболее часто встречающиеся слова и их количество.


    Пример вывода:
    Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
    sed: 2
    Lorem: 1

"""

from collections import Counter


def count_words(text):
    text_replace_split = text.lower().replace(",", "").replace(".", "").split()
    return Counter(text_replace_split).items()


user_input = input("Введите текст: ")
sort_words = sorted(count_words(user_input), key=lambda x: x[1], reverse=True)


for i in sort_words[:4]:  # подчет в диапазоне скольких слов
    print(f"{i[0]}: {i[1]}")
