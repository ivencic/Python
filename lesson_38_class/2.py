"""
    2. Создайте класс Student для представления студента. Класс должен иметь атрибуты name (имя) и age (возраст),
    а также метод display_info(), который выводит информацию о студенте.
    Затем создайте экземпляр класса Student с заданным именем и возрастом и вызовите метод display_info().
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)


n = input("Input student name: ")
a = input("Input student age: ")
student = Student(n, a)

student.display_info()
