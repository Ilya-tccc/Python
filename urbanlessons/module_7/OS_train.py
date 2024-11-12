import os
import time

directory = os.getcwd()
#
# if os.path.exists('train'):
#     os.chdir('train')
# else:
#     os.mkdir('train')
#

for root, dirs, files in os.walk(directory):
    # files= [f for f in os.listdir() if os.path.isfile(f)]
    for file in files:
        filepath = os.path.join(root,file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
