# 2. Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте классы Rectangle (прямоугольник) и Circle (круг). Класс Shape должен иметь абстрактный метод area, который должен быть реализован в каждом дочернем классе. Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра. Выведите площадь и периметр прямоугольника и круга на экран.
#
# Пример использования:
#
# rectangle = Rectangle(5, 3)
# circle = Circle(2)
#
# print(f"Rectangle area: {rectangle.area()}")  # Вывод: Rectangle area: 15
# print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Вывод: Rectangle perimeter: 16
# print(f"Circle area: {circle.area()}")  # Вывод: Circle area: 12.566370614359172
# print(f"Circle perimeter: {circle.perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return (self.w + self.h) * 2


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r


shapes = [Rectangle(5, 3), Circle(2)]
for item in shapes:
    print(f"Area: {item.area()}, Perimter: {item.perimeter()}")
