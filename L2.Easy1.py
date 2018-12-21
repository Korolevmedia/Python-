_author_='Andrey Korolev'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

#первый вариант решения
fruits = ["яблоко", "банан", "киви", "арбуз"]
n = 0
for fruit in fruits:
    n = n + 1
    print('{0}{1:<}{2:>7}'.format(n, '.', fruit))

#второй вариант решения (неточный)
fruits = ["яблоко", "банан", "киви", "арбуз"]
n = 0
for fruit in enumerate(fruits, 1):
    print(fruit)



