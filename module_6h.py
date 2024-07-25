class Figure:
    sides_count = 0

    def __init__(self, color=None, filled=False, *sides):
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        if color is None:
            color = [0, 0, 0]

        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=None, filled=False, *sides):
        if len(sides) == 0:
            sides = [1]
        super().__init__(color, filled, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        circumference = self.get_sides()[0]
        return circumference / (2 * 3.14)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=None, filled=False, *sides):
        if len(sides) == 0:
            sides = [1, 1, 1]
        super().__init__(color, filled, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        base = max(self.get_sides())
        return 2 * area / base

    def get_height(self):
        return self.__height

    def get_square(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=None, filled=False, *sides):
        if len(sides) == 0:
            sides = [6] * 12
        super().__init__(color, filled, *sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
