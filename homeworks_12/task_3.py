#3)	В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов
filename = "file.txt"
content = input("Введите содержимое файла: ")
with open(filename, "w") as file:
    file.write(content)
with open(filename, "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    for line in lines:
        char_count = len(line.strip())
        print(f"Количество символов в строке: {char_count}")

print(f"Общее количество строк: {line_count}")

