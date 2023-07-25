#Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку
string = 'An apple a day keeps the doctor away'
char_dict = {}
for char in string:
    if char not in char_dict:
        char_dict[char] = 1
    else:
        char_dict[char] += 1
print(char_dict)