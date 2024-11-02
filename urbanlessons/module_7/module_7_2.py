def custom_write(file_name,strings):
    file=open(file_name,'w',encoding='utf-8')
    res={}
    i=1
    for string in strings:
        res.update({(i,file.tell()):string})
        file.write(f'{string}\n',)
        i+=1
    file.close()
    return res


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

