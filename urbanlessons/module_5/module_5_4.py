from asyncio import run_coroutine_threadsafe
from tkinter.font import names


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(
                f'{new_floor} этажа не существует на объекте "{self.name}"')
        else:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Разные типы данных невозможно сравнить')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Разные типы данных невозможно сравнить')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Разные типы данных невозможно сравнить')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Разные типы данных невозможно сравнить')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Разные типы данных невозможно сравнить')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Разные типы данных невозможно сравнить')

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            print("Арифметические действия возможны только с числовым типом данных")
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __del__(self):
        print(f'{self} снесён, но он останется в истории')
        return


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
