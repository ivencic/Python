def word_len(text):

    words = text.split()  # Разбиваем строку на слова
    lengths = tuple(len(word) for word in words)  # Создаем кортеж длин слов
    return lengths

text = input("Введите предложение: ")

word_len = word_len(text)

print("Длины слов в предложении:", word_len)
