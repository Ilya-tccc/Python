first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(i) for i in first_strings if len(i) > 5]
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
third_result = {x: len(x) for x in (first_strings + second_strings) if len(x) % 2 == 0}
print(first_result, '\n', second_result, '\n', third_result)
