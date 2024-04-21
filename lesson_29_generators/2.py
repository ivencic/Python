"""
Напишите генератор, который будет генерировать арифметическую прогрессию
"""


def progress(a1, d, size):
    count = 1
    while count <= size:
        yield a1
        a1 += d
        count += 1


for i in progress(2, 6, 5):
    print(i)
