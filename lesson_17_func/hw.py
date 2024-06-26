"""
1. Напишите программу, которая принимает два числа и
возвращает их сумму и произведение в виде кортежа (sum, product).
Используйте функцию для вычисления суммы и произведения.
Выведите результат на экран с помощью команды print.

Пример вывода:

Введите первое число: 3
Введите второе число: 4

Сумма и произведение чисел: (7, 12)

"""


def calculate_sum_and_product(num1, num2):
    summ = num1 + num2
    prod = num1 * num2
    return summ, prod

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = calculate_sum_and_product(num1, num2)

print("Сумма и произведение чисел:", result)

"""
2. Напишите программу, которая принимает список чисел и 
возвращает сумму, минимальное и максимальное значение из списка. 
Используйте функцию для обработки списка чисел и возврата трех значений. 
Выведите результат на экран с помощью команды print.

Пример вывода:

Введите числа:  3, 7, 2, 9, 1, 5
Сумма чисел: 27
Минимальное значение: 1
Максимальное значение: 9
"""
def my_func(numbers):
    summ = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return summ, minimum, maximum

numbers = input("Введите числа, разделенные запятыми: ").split(',')

numbers = [int(num.strip()) for num in numbers]

summ, minimum, maximum = my_func(numbers)

# Вывести результат на экран
print("Сумма чисел:", summ)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)