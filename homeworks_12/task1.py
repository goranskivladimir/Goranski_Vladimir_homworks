#1)	Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала
# шли числа по возрастанию, а потом слова по возрастанию их длины
numbers = []
words = []
file = open('file1.txt','w')
content = input('Введите содержимое файла: ')
file.write(content)
with open('file1.txt', 'r') as file:
    for line in file:
        elements = line.split(' ')
        for i in elements:
            if i.isdigit():
                numbers.append(int(i))
            else:
                words.append(i)
numbers.sort()
words.sort(key=len)
result_list = numbers + words
print(numbers)
print(words)
print(result_list)






