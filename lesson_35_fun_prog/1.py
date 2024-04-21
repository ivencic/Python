"""
    1. Напишите функцию, которая принимает на вход список чисел и
    возвращает сумму квадратов только четных чисел из списка,
    используя функциональные подходы (например, map, filter и reduce).

Пример вывода:
Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
Результат: 72
"""

from functools import reduce


def sum_of_even_squares(nums):
    even_numbers = filter(lambda x: x % 2 == 0, nums)
    squared_numbers = map(lambda x: x ** 2, even_numbers)
    res = reduce(lambda x, y: x + y, squared_numbers, 0)
    return res


def input_numbers():
    numbers_str = input("Введите числа, разделенные запятыми: ")
    striped_str_to_int = [int(num.strip()) for num in numbers_str.split(",")]
    return striped_str_to_int


numbers = input_numbers()
result = sum_of_even_squares(numbers)
print("Результат:", result)
