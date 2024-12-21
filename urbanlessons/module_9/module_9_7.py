"""
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
"""
def is_prime(func):
    def wrapper(*args,**kwargs):
        n = func(*args,**kwargs)
        if n <= 1:
            print("сумма равна 1 или 0")
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("составное")
                break
        else:
            print("Простое")
        return n
    return wrapper

@is_prime
def sum_three(*args):
    res=sum(args)
    return res

result = sum_three(2, 3, 6)
print(result)