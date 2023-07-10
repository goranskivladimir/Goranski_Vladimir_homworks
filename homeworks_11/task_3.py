#3)	Есть список натуральных чисел. Требуется сформировать из них множество. Если какое-либо число повторяется,
# то преобразовать его в строку по образцу: например, если число 4 повторяется 3 раза,
# то в множестве будет следующая запись: само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
# строка «444» (третье повторение, т.е. строка множится на 3).
numbers = [1, 2, 3, 4, 4, 5, 4, 6, 6, 6,]
result_set = set()
for number in numbers:
        count = numbers.count(number)
        if count > 1:
            for i in range(1, count+1):
                result_set.add(str(number) * i)
        else:
            result_set.add(number)
print(result_set)