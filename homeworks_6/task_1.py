#"""1)	Дан список list=[15,48,'hello',6,19,'world’]. Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных. Вывести всё на экран"""
list = [15, 48, 'hello', 6, 19, 'world']
vowels = ['a', 'e', 'i', 'o', 'u']
print(list)
for i in list:
    if type(i) == int:
        if i % 2 == 0:
            sum = 0
            for j in str(i):
                sum += int(j)
            print('Число', i, "четное,Сумма его цифр :",sum)
        else:
            list[list.index(i)] = 1
            print('Число', i,'нечетное.Заменено на 1')
    elif type(i) == str:
        glas = 0
        for j in i:
            if j.lower() in vowels:
                glas +=1
        print('Слово',i,"содержит",glas,"гласных и",len(i) - glas, "согласных")



