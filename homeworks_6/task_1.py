#Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию
import random

numbers = random.randint(1, 10)
color = random.randint(1, 2)
if color == 1:
    color_str = 'красный'
else:
    color_str = 'черный'
attempt = 5
while attempt > 0:
    clr_num = input(f'Введите число и цвет  (осталось попыток : {attempt}): ')
    user_number, user_color = clr_num.split()
    user_number = int(user_number)
    if user_color == 'красный':
        user_color = 1
    else:
        user_color = 2
    if user_number == numbers and user_color == color:
        print('Вы выиграли')
        break
    else:
        print('Вы не угадали,попробуйте еще раз')
        attempt -= 1
    if attempt == 0:
        print(f'Вы проиграли!Число :{numbers}, цвет:{color} ')



