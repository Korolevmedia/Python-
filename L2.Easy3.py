_author_='Andrey Korolev'

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [2, 5, 8, 11, 13, 20]
b = []

for c in a:
    if c % 2 == 0:
        b.append(c / 4)
    else:
        b.append(c * 2)
print(b)


