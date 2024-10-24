import math


class Figure:
    sides_count = 0
    def __init__(self, __color,*__sides,filled=True):
        if self.__is_valid_sides(*__sides):
            self.__sides = __sides
        else:
            self.__sides=[1]*self.sides_count
        self.__color=__color
        self.filled=filled
    def get_color(self):
        return self.__color
    def __is_valid_color(self,r,g,b):
        if 0<=int(r)<+255 and 0<=int(g)<+255 and 0<=int(b)<+255:
            return True
        else:
            print('Такого цвета не существует')
            return False
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color=(r,g,b)
    def __is_valid_sides(self,*sides):
        if len(sides)==self.sides_count or (len(sides)==1 and isinstance(self,Cube)):
            for side in sides:
                if isinstance(side,int) and side>0:
                    continue
                else:
                    break
            else:
                return True
    def get_sides(self):
        return list(self.__sides)
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self,*sides):
        if self.__is_valid_sides(*sides):
            self.__sides=sides


class Circle(Figure):
    sides_count = 1
    def __radius(self):
        return sum(self.__sides)/(2*math.pi)
    def get_square(self):
        return 2*math.pi*self.__radius()

class Triangle(Figure):
    sides_count = 3
class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, __sides, filled=True):
        super().__init__( __color)
        self.__sides = [__sides]*self.sides_count
    def get_volume(self):
        res = math.prod(self.__sides)
        print(self.__sides)
        return res

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1=Triangle((200, 200, 100), 10, 6,7)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
print(triangle1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())