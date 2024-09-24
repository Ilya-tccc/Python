total_sum=0

def calculate_structure_sum(*args):
    global total_sum

    for i in range(len(args)):
        if isinstance(args[i],(int,float)):
            total_sum+=args[i]
        elif isinstance(args[i],dict):
            for key,value in args[i].items():
                calculate_structure_sum(key,value)
        elif isinstance(args[i],(list,tuple,set)):
            calculate_structure_sum(*args[i])
        elif isinstance(args[i],str):
            total_sum+=len(args[i])
    return    total_sum



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(f'Сумма всех чисел и длин элементов равна: {result}')

