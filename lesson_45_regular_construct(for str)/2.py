"""
    Напишите функцию highlight_keywords(text, keywords),
    которая выделяет все вхождения заданных ключевых слов в тексте,
    окружая их символами *.
    Функция должна быть регистронезависимой при поиске ключевых слов.

Пример использования:

text = "This is a sample text. We need to highlight Python and programming."

keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)
# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
"""

import re


def highlight_keywords(txt, keys):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(keyword)
                                           for keyword in keys) + r')\b', re.IGNORECASE)

    refact_text = pattern.sub(r'*\1*', txt)

    return refact_text


text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)


