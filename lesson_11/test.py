"""
2. Напишите программу, которая запрашивает у пользователя строку и
 выводит на экран количество гласных и согласных букв в ней.
 Используйте функцию len() для подсчета количества букв.
 Выведите результат на экран с помощью команды print. Решить задачу для латиницы.


Пример вывода:

Введите строку: Hello World

Количество гласных букв: 3
Количество согласных букв: 7
"""

in_text = input('Введите строку: ').lower()
glas = 'aeiouy'
sogl = 'bcdfghklmnpqrstvwxz'

low_text = in_text.lower()

i = 0
res_glas = 0
res_soglas = 0

while i < len(low_text):
    if low_text[i] in glas:
        res_glas += 1
    elif low_text[i] in sogl:
        res_soglas += 1
    i += 1
print('Количество гласных букв: ', res_glas)
print('Количество согласных букв: ', res_soglas)
