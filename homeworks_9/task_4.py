#4)	На вход программы подается словарь a = {1:10, 2:20, 3:30}, необходимо получить список произведения ключа на
# значение.
a = {1:10, 2:20, 3:30}
for key, value in a.items():
    print(f'Произведеине ключа {key} на значение {value}: {key * value} ')