def apply_all_func(int_list, *functions):
    res = {}
    for function in functions:
        res.update({function.__name__: function(int_list)})
    return res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
