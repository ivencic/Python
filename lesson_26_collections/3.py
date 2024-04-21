"""
    3.
    Напишите программу, которая принимает словарь от пользователя и ключ,
    и возвращает значение для указанного ключа с использованием
    метода get или setdefault. Создайте функцию get_value_from_dict,
    которая принимает словарь и ключ в качестве аргументов,
     и возвращает значение для указанного ключа,
     используя метод get или setdefault в зависимости от выбранного варианта.
     Выведите полученное значение на экран.

Пример словаря:
my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

Пример вывода:

Введите ключ для поиска: banana
Использовать метод get (y/n)? y
Значение для ключа 'banana': 6
"""


def get_value_from_dict(dictionary, key, method):
    if method:
        return dictionary.get(key)
    return dictionary.setdefault(key, 0)


initial_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

usr_key = input("Введите ключ для поиска: ")
meth = True if input("Использовать метод get (y/n)? ").lower() == "y" else False

print(f"Значение для ключа '{usr_key}': {get_value_from_dict(initial_dict, usr_key, meth)}")
