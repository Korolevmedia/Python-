_author_='Andrey Korolev'

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input('Enter the quantity of elements of list "b": '))
b = []

for c in range(n):
    c = random.randint(-100, 100)
    b.append(c)
print(b)

