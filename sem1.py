import math

# Решите квадратное уравнение 5x^2-10x-400=0 последовательно сохраняя переменные a, b, c, d, x1 и x2.
"""
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

try:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Корней нет")
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
except ZeroDivisionError:
    print("Ошибка: деление на ноль")

# Посчитайте сумму чётных элементов от 1 до n исключая кратные e. Используйте while и if.

n = int(input("Введите n: "))
e = int(input("Введите e: "))
suma = 0
i = 1
while i <= n:
  if i % 2 == 0 and i % e != 0:
    suma += i
  i += 1
print("Сумма чётных элементов от 1 до", n, "с исключением кратных", e, "равна", suma)

'''
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
'''

year = int(input("Введите год: "))

if year < 1582 or (year % 4 != 0 or year % 100 == 0 and year % 400 != 0):
    result = "обычный"
else:
    result = "високосный"

print(result)

'''
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
'''

while True:
    number = input("Введите число от 1 до 999: ")
    if len(number) == 1:
        square_number = int(number) ** 2
        result = f"Одна цифра, её квадрат: {square_number}"
    elif len(number) == 2:
        digit1, digit2 = int(number[0]), int(number[1])
        multiplication = digit1 * digit2
        result = f"Двузначное число, произведение цифр: {multiplication}"
    elif len(number) == 3:
        mirror_number = int(number[::-1])
        result = f"Трёхзначное число, зеркальное отображение: {mirror_number}"
    else:
        result = "Введено неподходящее число. Попробуйте ещё раз."

    print(result)

# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

rows = int(input("Введите количество рядов: "))
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

for i in range(2, 10):
    for j in range(2, 6):
        print(f"{i} X {j} = {i*j}", end='\t\t')
    print('\n')
print()
for i in range(2, 10):
    for j in range(6, 10):
        print(f"{i} X {j} = {i*j}", end='\t\t')
    print('\n')

"""