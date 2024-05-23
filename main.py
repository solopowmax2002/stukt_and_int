from abc import ABC, abstractmethod


# Абстрактный класс
class Shape(ABC):
    def __init__(self, radius):
        self.radius = radius

    @abstractmethod
    def area(self):
        pass


# Класс круга, наследующийся от абстрактного класса Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return 3.14 * self.radius ** 2


# Абстрактный класс Drawable
class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass


# Класс круга, реализующий интерфейс Drawable
class CircleDrawer(Drawable):
    def draw(self):
        print("Drawing a circle")


class QuadrateDrawer(Drawable):
    def draw(self):
        print("Drawing a quadrate")


circle = Circle(5)
print(circle.area())

circle_drawer = CircleDrawer()
circle_drawer.draw()

quadrate_drawer = QuadrateDrawer()
quadrate_drawer.draw()
