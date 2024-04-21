# 1.

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))


print('Сумма: ', first_number + second_number)
print('Разность: ', first_number - second_number)
print('Произведение: ', first_number * second_number)
print('Частное: ', first_number / second_number)
print('Остаток от деления: ', first_number % second_number)
print('Первое число в степени второго числа: ',first_number ** second_number)

# 2.

r = float(input('Введите радиус окружности: '))
pi = 3.141592653589793
long = 2 * pi * r
area = pi * r ** 2

print('Длина окружности: ', long)
print('Площадь окружности: ', area)

# 3.

first = input('Введите координаты первой точки (x1, y1): ')
second = input('Введите координаты второй точки (x2, y2): ')

x1 = float(first[0])
y1 = float(first[-1])
x2 = float(second[0])
y2 = float(second[-1])

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print('Расстояние между точками: ', distance)

