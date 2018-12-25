_author_='Andrey Korolev'

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = ['apple', 'kiwi', 'orange', 'apple']
print("Список:" , a)
b = input('Введите слово, которое стоит исключить из списка: ')

def myfilter(a, b):
    for i in a:
        if b in a:
            a.remove(b)
    print(a)

myfilter(a, b)
