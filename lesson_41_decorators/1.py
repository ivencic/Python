"""
    1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и
    выводить сообщение об ошибке, если переданы аргументы неправильного типа.
    Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.

Пример использования:

@validate_args(int, str)
def greet(age, name):
print(f"Привет, {name}! Тебе {age} лет.")
greet(25, "Анна")  # Все аргументы имеют правильные типы
greet("25", "Анна")  # Возникнет исключение TypeError

Ожидаемый вывод:

Привет, Анна! Тебе 25 лет.
TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.

"""


def validate_args(*t):
    def valid_args(func):
        def wrapper(*args):
            for i in range(len(t)):
                if type(args[i]) is not t[i]:
                    raise TypeError(f"Аргумент {args[i]} имеет неправильный тип"
                                    f"{type(args[i])}. Ожидается {t[i]}.")
            func(*args)

        return wrapper

    return valid_args


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


greet(25, "Anna")

greet("25", "Anna")
