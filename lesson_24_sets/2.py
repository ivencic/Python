"""
    2.
    Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет,
    является ли set1 подмножеством set2.
    Функция должна возвращать True, если все элементы из set1 содержатся в set2,
    и False в противном случае.
    Функция должна быть реализована без использования встроенных методов issubset или <=.

Пример множеств

{1, 2, 3}
{1, 2, 3, 4, 5}

Пример вывода:
True

"""
def is_subset(s1, s2):
    positiv = True
    for i in s1:
        if i not in s2:
            positiv = False
    return positiv

set1 = set(input("SET 1: "))
set2 = set(input("SET 2: "))

print(is_subset(set1, set2))

