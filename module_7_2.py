def custom_write(file_name, strings):
    dec = {}
    i = 1
    file = open(file_name, 'w', encoding='utf-8')
    for s in strings:
        dec[(i, file.tell())] = s
        file.write(str(s) + '\n')
        i += 1
    file.close()

    return dec


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
