#Ввести 10 чисел с клавиатуры, данные числа добавить во множество
numbers_set = set()
for i in range(10):
    number = int(input("Введите число: "))
    numbers_set.add(number)
print("числа в множестве:", numbers_set)