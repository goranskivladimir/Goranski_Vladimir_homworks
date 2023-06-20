# 4)	Пользователь вводит два числа с клавиатуры. Вывести на экран yes,
# если они отличаются друг от друга на 135, иначе вывести на экран No
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
if first_number - second_number == 135:
    print('yes')
else:
    print('no')
