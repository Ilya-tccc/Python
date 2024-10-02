class House:
    def __init__(self, name, umber_of_floors):
        self.name = name
        self.number_of_floors = umber_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(
                f'{new_floor} этажа не существует на объекте "{self.name}"')  # По заданию необходимо вывести просто 'Такого этажа не существует', но сделал более информативный вывод
        else:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
