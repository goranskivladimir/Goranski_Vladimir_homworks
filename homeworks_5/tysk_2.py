#Есть список с четными и нечетными элементами. Посчитать количество четных и нечетных элементов.
list1 = 0
list2 = 0
for i in range(1, 100):
    if i % 2 != 0:
        list1 += 1
    if i % 2 == 0:
        list2 += 1


print('Количество нечетных чисел в списке list1: ', list1)
print('Количество четных чисел в списке list2: ', list2)