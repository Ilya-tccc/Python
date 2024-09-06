immutable_var= 1, 2,3,4,5,True,'apple'
print(immutable_var)
#immutable_var[0]=2#"Элементы кортежа не могут быть изменены, т.к. так заложено программой для органичения возможности корректировки набора данных
mutable_list= [1, 2,3,4,5,True,'apple']
mutable_list[1]='sun'
mutable_list.insert(3,'tree')
mutable_list.append(False)
print(mutable_list)

