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
