from operator import index


def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function() Вызов невозможен, т.к. функция определена только в пределах функции test_function
import math, datetime

a=math.sin(60)

b=datetime.datetime
print(a,b)
a=1
b=15
c=True

print(id(a), id(b),id(c))

if a is c:
    print("same type")
if a==b:
    print("same value")

from .pack_2 import hi

