"""
    2. Напишите функцию, которая принимает на вход список функций и значение,
    а затем применяет композицию этих функций к значению, возвращая конечный результат.

Пример использования:
add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3

functions = [add_one, double, subtract_three]
compose_functions(functions, 5) должно вывести 9

"""


def compose_functions(funcs, value):
    res = value
    for func in funcs:
        res = func(res)
    return res


add_one = (lambda x: x + 1)
double = (lambda x: x * 2)
subtract_three = (lambda x: x - 3)

val = int(input("Input num of values: "))
functions = [add_one, double, subtract_three]
result = compose_functions(functions, val)
print(f"Res = {result}")  # Выведет 9
