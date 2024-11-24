first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для вычисления разницы длин строк, если длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк без использования zip
second_result = ((len(first[i]) == len(second[i])) for i in range(len(first)))


# Проверка (необязательно, для демонстрации работы)
print("First result:", list(first_result)) # Преобразуем генератор в список для вывода
print("Second result:", list(second_result)) # Преобразуем генератор в список для вывода