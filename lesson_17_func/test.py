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
