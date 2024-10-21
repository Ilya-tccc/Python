class Horse():
    # def __init__(self,x_distance = 0, sound = 'Frrr'):
    #     self.x_distance=x_distance
    #     self.sound=sound
    x_distance = 0
    sound = 'Frrr'

    # y_distance=super().y_distance
    def __str__(self):
        return f'Пройдено {self.x_distance} со звуком {self.sound}'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    # def __init__(self):
    #     self.y_distance = 0
    #     self.sound = 'I train, eat, sleep, and repeat'
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    def __init__(self):
        self.sound = super().sound
        self.x_distance = super().x_distance
        self.y_distance = super().y_distance

    def move(self, dx, dy):
        super().fly(dy)
        super().run(dx)

    def get_pos(self):
        tuple_ = (self.x_distance, self.y_distance)
        return tuple_

    def voice(self):
        print(super().sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
print(Pegasus.mro())
