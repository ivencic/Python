#  1.
"""
Напишите программу, которая принимает список чисел от пользователя и
передает его в функцию modify_list, которая изменяет элементы списка.
Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
Выведите измененный список на экран.
Объясните, почему изменения происходят только внутри функции и как работают изменяемые и
неизменяемые параметры.

Пример вывода:

Введите список чисел, разделенных пробелами: 1 2 3 4 5
Измененный список чисел: [2, 1, 6, 2, 10]
"""


def modify_list(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i] //= 2
        else:
            nums[i] *= 2


nums_input = input("Введите список чисел, разделенных пробелами: ")
ints = [int(x) for x in nums_input.split()]
modify_list(ints)
print("Измененный список чисел:", ints)

#  2.
"""
Напишите программу, которая принимает произвольное количество аргументов от пользователя
и передает их в функцию calculate_sum, которая возвращает сумму всех аргументов.
Используйте оператор * при передаче аргументов в функцию. Выведите результат на экран.

Пример вывода:

Введите числа, разделенные пробелами: 1 2 3 4 5
Сумма чисел: 15

"""


def calculate_sum(*args):
    return sum(args)


user_input = input("Введите числа, разделенные пробелами: ")
numbers = [int(i) for i in user_input.split()]
print("Сумма чисел:", calculate_sum(*numbers))