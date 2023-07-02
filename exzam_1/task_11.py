#11.Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”]. В новый список добавить элементы,
# которые содержат пробел
str = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_str = []
for string in str:
    if " " in string:
        new_str.append(string)
print(new_str)
