# Перемножить все нечётные значения в диапазоне от 1 до 100
list1 = 1
for i in range(1, 100):
    if i % 2 != 0:
        print(i)
        list1 *= i
print(list1)


