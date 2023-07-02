#13.Дан список чисел, необходимо удалить все вхождения числа 20 из него
numbers = [1, 20, 20, 10, 15, 20, 35, 45]
numbers = [num for num in numbers if num != 20]
print(numbers)