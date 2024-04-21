"""
    1. Напишите программу, которая открывает файл,
       считывает из него два числа и выполняет операцию их деления.
       Если число отрицательное, выбросите исключение ValueError
       с сообщением "Число должно быть положительным".
       Обработайте исключение и выведите соответствующее сообщение.


"""

try:
    file = open("file.txt", 'r')
    num1 = float(file.readline())
    num2 = float(file.readline())
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Число должно быть положительным")
    result = num1 / num2
    print(f"Результат деления: {result}")
    file.close()
except FileNotFoundError:
    print("Файл не найден")

except ValueError as e:
    print(f"Ошибка: {e}")
except ZeroDivisionError:
    print("Деление на ноль невозможно")

