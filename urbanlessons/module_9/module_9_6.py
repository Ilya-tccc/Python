'''
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
print(i)
'''


def all_variants(text):
    n = len(text)
    for i in range(1 << n):
        variant = ""
        for j in range(n):
            if (i >> j) & 1:
                variant += text[j]
        yield variant

a = all_variants("abc")
for i in a:
    print(i)