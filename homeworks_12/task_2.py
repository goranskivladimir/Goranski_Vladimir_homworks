#2)	Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть
# служит пустая строка
file_name = 'file.txt'
with open(file_name, 'w') as file:
    while True:
        line = input('Введите строку: ')
        if line == '':
            break
        file.write(line + '\n')