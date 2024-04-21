"""
1. Напишите программу, которая генерирует случайное число от 1 до 100,
а затем предлагает пользователю угадать это число. Если пользователь угадывает число,
программа выводит сообщение о победе. Если пользователь не угадывает число,
 программа сообщает, больше или меньше загаданное число и предлагает попробовать снова.
 Используйте цикл с инструкцией break, чтобы остановить выполнение цикла, когда число угадано.

Пример вывода:

Угадайте число от 1 до 100: 50
Загаданное число меньше.
Попробуйте снова: 75
Загаданное число больше.
Попробуйте снова: 63
Поздравляю! Вы угадали число 63!

"""
import random

rand = random.randint(1,100)

ansver = int(input('Угадайте число от 1 до 100: '))


while True:
    if ansver < rand:
        print('Загаданное число меньше.')
        ansver = int(input('Попробуйте снова: '))
    elif ansver > rand:
        print('Загаданное число больше.')
        ansver = int(input('Попробуйте снова: '))
    else:
        break
print('Поздравляю! Вы угадали число ', rand)

"""
2. Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи. 
 Числа Фибоначчи - это последовательность чисел, где каждое следующее число является суммой двух предыдущих чисел (начиная с 0 и 1).
Используйте цикл while для решения задачи. Выведите числа через запятую с помощью команды print.

Пример вывода:
Введите число N: 7
Первые 7 чисел Фибоначчи: 0, 1, 1, 2, 3, 5, 8
"""
n = int(input("Введите число N: "))

a = 0
b = 1
fib = [0, 1]
count = 0
summ = 0

if n == 0:
    print('Первые', n, 'чисел Фибоначчи: ')
elif n == 1:
    print('Первые', n, 'чисел Фибоначчи: 0')
else:
    while count < n - 2:
        summ = a + b
        a = b
        b = summ
        fib.append(b)

        count += 1
    print('Первые', n, 'чисел Фибоначчи: ', end='')
    print(*fib, sep=', ')

"""
3. Напишите программу, которая запрашивает у пользователя целое положительное число 
   и проверяет, является ли оно простым.
   Простое число - это число, которое делится только на 1 и на само себя без остатка.
   Используйте цикл while и проверку деления числа на все числа от 2 до N-1 для решения задачи. 
   Выведите соответствующее сообщение на экран с помощью команды print.

Пример вывода:

Введите целое положительное число: 17

Число 17 является простым.

"""

number = int(input('Введите целое положительное число: '))
count = 2
egal = 0
res = number % count
while count < number:
    if egal == res:
        break
    else:
        count += 1
else:
    print('Число', number, 'является простым.')