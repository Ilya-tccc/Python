grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students)
students.sort()
students=tuple(students)#перевел в кортеж, чтобы не было возможности изменить отсортированные данные.Понимаю, что это необязательно
avarage_grades=[]
#avarage_grades.append([sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])])
avarage_grades.extend([sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])])
#avarage_grades[1]=sum(grades[1])/len(grades[1])
#avarage_grades[2]=sum(grades[2])/len(grades[2])
#avarage_grades[3]=sum(grades[3])/len(grades[3])
#avarage_grades[4]=sum(grades[4])/len(grades[4])
#print(avarage_grades)
students_grades=dict(zip(students, avarage_grades))
print(students_grades)
#print('Введите имя студента')
#name=str(input())
#print(students_grades.get(name))

#average_grades = {}
#for i, student in enumerate(students):
#    average_grades[student] = sum(grades[i]) / len(grades[i])
#print(average_grades)


