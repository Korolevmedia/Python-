_author_='Andrey Korolev'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a = [2, 27, -10, 4, -9]
c = [r for r in a if r % 3 == 0 and r > 0 and r % 4 != 0]
print(c)





