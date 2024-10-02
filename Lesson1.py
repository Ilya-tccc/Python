# #1st program
# print(9**0.5*5)
# #2st program
# print(9.99>9.98 and 1000!=1001)
# #3rd program
# print(2+2*2)
# print((2+2)*2)
# print(2+2*2<(2+2)*2)
# #4th program
# print(int(123.4568*10%10))
print((max(len("hi"), len("world")) + min(len("hi"), len("world"))) / 2)
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(isinstance(a, list)) # True
print(a == b) # True
print(a is b) # ???
print(id(a),id(b),id(c))
print(a is c) # ???
dict_={'a':[2,3,4,5,3],'b':2345235}
print(*dict_.pop('a'))