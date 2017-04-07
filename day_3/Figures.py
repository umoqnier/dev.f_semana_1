from math import pi


class Figure():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Rectangle(Figure):

    def __init__(self, name, height, width):
        super().__init__(name)
        self.height = height
        self.width = width

    def get_perimeter(self):
        return "The perimeter of the %s is %.2f " % (str(self.get_name()), (2 * self.height) + (2 * self.width))

    def get_area(self):
        return "The area of the %s is %.3f " % (str(self.get_name()), self.height * self.width)


class Square(Rectangle):

    def __int__(self, name, height):
        super().__init__(name, height)

    def get_perimeter(self):
        return "The perimeter of the %s is %.2f " % (str(self.get_name()), (4 * self.height))

    def get_area(self):
        return "The area of the %s is %.3f " % (str(self.get_name()), self.height ** 2)


class Circle(Figure):

    def __init__(self, name, radium):
        super().__init__(name)
        self.radium = radium

    def get_perimeter(self):
        return "The perimeter of the %s is %.3f " % (str(self.get_name()), pi * 2 * self.radium)

    def get_area(self):
        return "The area of the %s is %.3f " % (str(self.get_name()), pi * self.radium ** 2)

if __name__ == '__main__':
    rectangle = Rectangle('Rectangulin', 30, 10)
    circle = Circle('Circulin', 15)
    square = Square('Cuadradin', 10)

    print("Information of : ", rectangle.get_name())
    print(rectangle.get_perimeter())
    print(rectangle.get_area(), "\n")
    print("Information of : ", circle.get_name())
    print(circle.get_perimeter())
    print(circle.get_area(), "\n")
    print("Information of : ", square.get_name())
    print(square.get_perimeter())
    print(square.get_area())