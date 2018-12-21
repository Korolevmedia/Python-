_author_='Andrey Korolev'

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print("Let's solve the equation a*x*x + b*x + c = 0")
a = int(input('Enter the value of variable "a": '))
if a != 0:
    b = int(input('Enter the value of variable "b": '))
    c = int(input('Enter the value of variable "c": '))
    d = b*b - 4*a*c
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        print('"x1" = ', x1)
        print('"x2" = ', x2)
    elif d == 0:
        x1 = -b / (2*a)
        x2 = x1
        print('"x1"="x2" = ', x1)
    else:
        print('There are no any roots of equation')
else:
    print('You must enter the value of variable "a" different from "0" ')
