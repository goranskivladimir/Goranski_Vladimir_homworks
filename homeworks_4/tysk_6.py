#Пользователь покупает автомобиль стоимость 100000 рублей.
# Если денег на счету достаточно, нужно списать деньги и вывести сообщение: ‘Поздравляю, вы купили автомобиль!!!’,
# а иначе вывести ‘У вас недостаточно средств для покупки автомобиля’. Не забульте пожелать ‘Хорошего дня’ в любом случае
money = int(input('Введите сумму: '))
if money >= 100000:
    print('Поздравляем с покупкой автомобиля!Хорошего дня')
else:
    print('К сожалению на счету не достаточно средств.Хорошего вам дня!')