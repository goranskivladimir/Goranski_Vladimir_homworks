#15.Необходимо удалить пустые строки из списка строк.
strings = ["", 'Hello', "", 'world', "","", 'where you from?']
new_string = [string.strip() for string in strings if string.strip()]
print(new_string)