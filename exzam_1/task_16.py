
string = input("Введите строку: ")
string = string.lower()
length = len(string)
g_count = string.count('g')
c_count = string.count('c')
gc_percentage = (g_count + c_count) / length * 100
print(f"Процентное содержание символов G и C: {gc_percentage}%")