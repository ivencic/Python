#  1.
"""
    Напишите программу, которая принимает матрицу (вложенный список)
    от пользователя и находит сумму всех элементов в матрице.
    Используйте вложенные списки и циклы для обхода элементов матрицы.


Пример матрицы: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Пример вывода:
Сумма элементов в матрице: 45
"""
s = input("Пример матрицы: ")
s = s.replace("[", "")
s = s.replace("]", "")
s = s.replace(",", "")
s = s.replace(" ", "")
s = list(s)
new_s = [int(i) for i in s]
print(sum(new_s))

###   Это код если пользыватель введет имеено список из ИНТОВ
"""a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum = 0

for sublist in a:
    for num in sublist:
        total_sum += num
print("Сумма всех элементов списка:", total_sum)"""


#  2.
"""
Напишите программу, которая принимает список чисел от пользователя и
сортирует его в порядке убывания, используя метод sort() и параметр reverse=True.
Выведите отсортированный список на экран.

Пример вывода:

Введите список чисел, разделенных пробелами: 5 2 8 1 3
Отсортированный список чисел: [8, 5, 3, 2, 1]

"""
l1 = input("Введите список чисел, разделенных пробелами: ").split()
l2 = [int(i) for i in l1]
l2.sort(reverse=True)
print(l2)

