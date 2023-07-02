# 1.Используя стандартные арифметические операции представьте самое большое целое число из цифр 4, 4, 4 и приведите его
# значение.
num1 = 4
num2 = 4
num3 = 4
sum = num1 + num2 + num3
sub = num1 - num2 - num3
mult = num1 * num2 * num3
div = num1 // num2 // num3
if sum > sub and sum > mult and sum > div:
    print(f'Наибольшие результат получаем с помощью сложения: {sum}')
elif sub > mult and sub > div:
    print(f'Наибольший результат мы получаем с помощью вычитания: {sub}')
elif mult > div:
    print(f'Наибольший результат мы получаем с помощью умножения: {mult}')
else:
    print(f'Наибольший результат мы получаем с помощью деления: {div}')

