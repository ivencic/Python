a = int(input('Введите натуральное десятичное число: '))
res = []
while (a // 2) < a:
    digit = a % 2
    res.append(digit)
    a = a // 2
b = reversed(res)
print('Двоичное представление числа: ', *b, sep='')
