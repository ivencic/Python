"""
1.  Напишите функцию merge_dicts,
    которая принимает произвольное количество словарей в качестве аргументов и
    возвращает новый словарь, объединяющий все входные словари.
    Если ключи повторяются, значения должны быть объединены в список.
    Функция должна использовать аргумент **kwargs для принятия
    произвольного числа аргументов словаря.

Пример ввода:
{'a': 1, 'b': 2}
{'b': 3, 'c': 4}
{'c': 5, 'd': 6}

Пример вывода:

{'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}


"""


def merge_dicts(*args):
    result = {}
    for d in args:
        for key, value in d.items():
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = value
    return result


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

new_dict = merge_dicts(dict1, dict2, dict3)
print(new_dict)
