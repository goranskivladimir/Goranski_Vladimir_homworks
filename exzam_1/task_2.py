#3.Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений
import math
def calculate_y(a, b, i):
    sin1 = math.sin(a + b - i)
    sin2 = math.sin(b + i - a)
    sin3 = math.sin(i + a - b)
    sin4 = math.sin(a + b + i)
    y = 1 / 4 * (sin1 + sin2 + sin3 - sin4)
    return y
a = 1
b = 2
i = 1
result = calculate_y(a, b, i)
print(result)