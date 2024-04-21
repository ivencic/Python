"""
1. Написать программу, вычисляющую факториал числа.

Решить задачу с помощью рекурсии.

"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        factorial(n-1)
    return n * factorial(n-1)


print(factorial(int(input("Enter num: "))))



