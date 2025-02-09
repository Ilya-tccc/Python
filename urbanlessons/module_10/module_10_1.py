'''Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.
'''
import time
import threading

def write_words(word_count, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for count in range(word_count):
                line = f'Какое-то слово № {count + 1}'
                file.write(line + '\n')
                time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
    except Exception as e:
        print(f"Ошибка при записи в файл {file_name}: {e}")

start=time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish=time.time()
print(f'Затраченное время {finish-start}')

start=time.time()
tread1=threading.Thread(target=write_words,args=(10, 'example5.txt'))
tread2=threading.Thread(target=write_words,args=(30, 'example6.txt'))
tread3=threading.Thread(target=write_words,args=(200, 'example7.txt'))
tread4=threading.Thread(target=write_words,args=(100, 'example8.txt'))
treads=[tread1,tread2,tread3,tread4]
for tread in treads:
    tread.start()
for tread in treads:
    tread.join()
finish=time.time()
print(f'Затраченное время {finish-start}')
