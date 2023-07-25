#Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.
def find_elements_below_average(numbers):
    average = sum(numbers) / len(numbers)
    result = []
    for num in numbers:
        if num < average:
            result.append(num)
    return result
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
below_average_elements = find_elements_below_average(my_list)
print(below_average_elements)