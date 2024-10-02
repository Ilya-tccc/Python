from itertools import count

example = 'Разработка'
print(example[:1])
print(example[:-1])
print(example[len(example)//2:])#По заданию необходимо вывести нечетное кол-во символов, но как это сделать автоматически пока непонятно, поэтому просто берем за данность, что у меня слово имеет четное количество символов.
print(example[::-1])
print(example[::2])

FIO='''Иванов
Иван 
Иванович'''
print(FIO)