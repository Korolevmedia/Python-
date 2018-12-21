_author_='Andrey Korolev'

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = [2, 4, 5, 7, 8]
b = [2, 7, 8, 11, 15]
c = set(a)
d = set(b)
f = c.difference(d)
print(list(f))
print()

# второе решение через цикл
for element in b:
    while element in a:
        a.remove(element)
print(a)
print(a[0])







