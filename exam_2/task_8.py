#Напишите программу, которая подключает модуль math и, используя значение числа \pi
# из этого модуля, вводим радиус круга  и находим периметр этого круга, результат вывести на экран
import math

radius = float(input("Введите радиус круга: "))
perimeter = 2 * math.pi * radius
print(f"Периметр круга: {perimeter}")