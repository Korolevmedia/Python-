_author_='Andrey Korolev'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ['apple', 'orange', 'kiwi', 'grape']
b = ['pineapple', 'peach', 'grape', 'apple', 'kiwi']

#первый вариант решения
d = [q for q in a for i in b if q == i]
print(d)

#второй вариант решения
t = [q for q in a if q in b]
print(t)






