#Дан список чисел. Если число встречается более двух раз, то добавить его в новый список
list1 = [1, 2, 4, 5, 6, 7, 3, 3, 1, 2, 5, 6, 10, 'hello',1, 2, 5, 6, 10, 'hello',1, 2, 5, 6, 10, 'hello', ]
list2 = []
for i in list1:
    item = False
    for x in list2:
        if x == i:
            item = True
            break
    if not item:
        list2.append(i)
print(list2)




