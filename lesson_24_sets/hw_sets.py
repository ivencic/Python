"""
    1.
    Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
    Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
    Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
    Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.


Пример переданного списка слов:


['cat', 'dog', 'tac', 'god', 'act']

Пример вывода:

Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']"""


def anagrams(args):
    anagram = []
    s = set()

    for word in args:
        sort = ''.join(sorted(word))
        if sort not in s:
            a = [w for w in args if ''.join(sorted(w)) == sort]
            anagram.append(a)
            s.add(sort)

    return anagram


words = eval(input("Input your list of word: "))
# можно и методами строк replace, потом через цикл добавлять, но так короче :)

result = anagrams(words)

print("Анаграммы:", *result)

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
    res = True
    for i in s1:
        if i not in s2:
            res = False
    return res


set1 = set(input("SET 1: "))
set2 = set(input("SET 2: "))

print(is_subset(set1, set2))
