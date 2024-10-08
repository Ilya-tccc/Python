class House:
    def __init__(self, name, umber_of_floors):
        self.name = name
        self.number_of_floors = umber_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor} этажа не существует на объекте "{self.name}"') # По заданию необходимо вывести просто 'Такого этажа не существует', но сделал более информативный вывод
        else:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)