'''Задача "За честь и отвагу!":
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
Атрибут name - имя рыцаря. (str)
Атрибут power - сила рыцаря. (int)
А также метод run, в котором рыцарь будет сражаться с врагами:
При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
В процессе сражения количество врагов уменьшается на power текущего рыцаря.
По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
Пункты задачи:
Создайте класс Knight с соответствующими описанию свойствами.
Создайте и запустите 2 потока на основе класса Knight.
Выведите на экран строку об окончании битв.
'''
import threading
import time


class Knight(threading.Thread):

    def __init__(self,name,power):
        threading.Thread.__init__(self)
        self.name=name
        self.power=power

    def run(self):
        print(f'{self.name},на нас напали!')
        # print(time.ctime())
        enemy=100
        day=0
        while enemy>0:
            enemy-=self.power
            time.sleep(1)
            # print(time.ctime())
            day+=1
            enemy = 0 if enemy < 0 else enemy
            if day%10==1:
                print(f'Рыцарь {self.name} сражается {day} день, осталось {enemy} воинов ')
            elif day%10==0:
                print(f'Рыцарь {self.name} сражается {day} дней, осталось {enemy} воинов ')
            elif day%10<5:
                print(f'Рыцарь {self.name} сражается {day} дня, осталось {enemy} воинов ')
            else:
                print(f'Рыцарь {self.name} сражается {day} дней, осталось {enemy} воинов ')
        else:
            print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы окончены!")