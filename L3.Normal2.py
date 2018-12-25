_author_='Andrey Korolev'

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(forsort):
    k = 1
    while k < len(forsort):
        for i in range(len(forsort)-k):
            if forsort[i] > forsort[i+1]:
                 forsort[i], forsort[i+1] = forsort[i+1], forsort[i]
        k = k + 1
    print(forsort)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

