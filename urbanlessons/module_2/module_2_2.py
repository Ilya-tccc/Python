first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third:
    print('Все 3 числа равны')# print(3)
elif first == second or first == third or second == third:
    print('2 числа из трех равны')# print(2)
# elif first!=second and first!=third and second!=third:
#     print('Все числа не равны')# print(0)
else:
    print('Все числа не равны')# print(0)