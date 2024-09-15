n = int(input('Число на левом столбе:'))
password = []
for i in range(1, n):
    for j in range(1, 21):
        if i == j:
            continue
        elif n % (i + j) == 0 and (i + j) <= n:
            password.append([i, j])
            continue
        else:
            continue
list_password = []
for i in password:
    i.sort()
    if i not in list_password:
        list_password.append(i)
    else:
        continue
unic_password =''
for i in range(len(list_password)):
    for j in range(len(list_password[i])):
        unic_password+=(str(list_password[i][j]))


print(password)
print('Пароль для числа ', n,'равен', unic_password)
