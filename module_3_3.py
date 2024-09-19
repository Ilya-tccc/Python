def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# задание 1
print_params()
print_params([1, 344], 1, 'man')
print_params(b=25)
print_params(c=[1, 2, 3])

# Задание 2
values_list = [1, 4.5, [8, True, 'string']]
values_dict = {'a': 1, 'b': 'строка', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# задание 3
values_list_2 = [4, 'string']
print_params(*values_list_2, 42)
