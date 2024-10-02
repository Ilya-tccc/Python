my_dict={'Sasha':1994,'Anna':2001}
print(my_dict)
print(my_dict['Anna'],my_dict.get('Alex','Такого ключа нет'))
my_dict.update({'Alex':2003, 'Tom':1990})
print(my_dict)
print('Anna:',my_dict.pop('Anna')) #Если я правильно понял, то достаточно было вывести только значение пары, но информативнее, если сначала вывести ключ, который все равно указывается в .pop
print(my_dict)

my_set={1,3,3,4,14,5,5,51,2,34,4,True,False,'POP'}
print(my_set)# Не понял, почему не выводится значение True
#my_set.add({'HJH',(1,3,4,5)})#Не понял, можно ли добавить несколько значений через .add
my_set.update({2,421,114,(1,3,4,5),(1,2)})
my_set.remove(1)
#my_set.difference_update({1,2,3,(1,2),False})
print(my_set)