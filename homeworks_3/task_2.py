#"""Разделить строку  “Apples, Oranges, Pears, Bananas, Berries” по запятым и вывести на экран,затем
# Затем объединить элементы с использованием пробела, чтобы программа вывела “Apples Oranges Pears Bananas Berries”"""

string_1 =  'Apples Oranges Pears Bananas Berries'
str2 = string_1.split(" ")
print(str2)
str3 = " ".join(str2)
print(str3)