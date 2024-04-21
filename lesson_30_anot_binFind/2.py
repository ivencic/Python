"""
    Напишите программу, которая будет считывать данные о продуктах из файла
    и использовать аннотации типов для аргументов и
    возвращаемых значений функций. Создайте текстовый файл "products.txt",
    в котором каждая строка будет содержать информацию о продукте в формате "название, цена, количество".

Например:
Apple, 1.50, 10
Banana, 0.75, 15

В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую стоимость.
Продумайте, какая аннотация должна быть у аргумента!
Считайте данные из файла, разделите строки на составляющие и
создайте список продуктов. Затем вызовите функцию calculate_total_price с этим списком и выведите результат.



Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода.
Потому что в реальных задачах обычно этого нет. Нужно самому придумывать даже самые простые тестовые данные,
содержимое тестовых файлов и т.п. В случае с классами (будут чуть позже) особенно.
"""


from typing import List, Tuple


def calculate_total_price(products: List[Tuple[str, float, int]]) -> float:
    total_price = 0
    for product in products:
        _, price, quantity = product
        total_price += price * quantity
    return total_price


def r_file():
    products = []
    with open('products.txt', 'r') as file:
        for line in file:
            name, price, quantity = line.strip().split(', ')
            products.append((name, float(price), int(quantity)))

    total_price = calculate_total_price(products)
    print(f'Total price: {total_price}')


r_file()
