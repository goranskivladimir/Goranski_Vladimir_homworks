# 4)	Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом,
# то должна выполняться конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются
value1 = input('Введите первое значение: ')
value2 = input('Введите второе значение: ')
if value1.isdigit() and value2.isdigit():
    result = int(value1) + int(value2)
else:
    result = str(value1) + str(value2)

print(result)