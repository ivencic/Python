#  1.
#  create func
def filter_students(s, bal):
    new_list = []
    for student in s:
        if student[2] > bal:
            new_list.append(student[0])
    return new_list

# func str to list
def str_list(s):
    s = s.replace("),", ").")
    s = s.replace("[", "")
    s = s.replace("]", "")
    s = s.split("; ")
    for i in range(s):
        s[i] = s[i].replace("(", "")
        s[i] = s[i].replace(")", "")
        a, b, c = s[i].split(", ")
#  inputs
s = input("Введите список кортежей студентов: ")
bal = int(input("Введите пороговое значение среднего балла: "))

#  call func (2 inputs arguments)
filtered_students = filter_students(s, bal)

print("Студенты с средним баллом выше", bal, ":", filtered_students)


# 2.
def word_len(text):
    words = text.split()  # Разбиваем строку на слова
    lengths = tuple(len(word) for word in words)  # Создаем кортеж длин слов
    return lengths


text = input("Введите предложение: ")

word_len = word_len(text)

print("Длины слов в предложении:", word_len)
