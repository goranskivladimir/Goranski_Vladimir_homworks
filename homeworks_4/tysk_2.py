#Определить существование треугольника.А так же его тип
print('Стороны')
a = int(input('Введите сторону "а": '))
b = int(input('Введите сторону "b": '))
c = int(input('Введите сторону "c": '))
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольника не существует")
elif a == b and a == c:
    print("Треугольник равносторонний")
elif a == b or a == c or b == c:
    print('Треугольник равнобедренный')
else:
    print("Треугольник не существует")
