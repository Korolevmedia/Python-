# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 1
    b = 0
    i = 0
    for i in range(m):
        fib = a + b
        a = b
        b = fib
        print(fib)

fibonacci(1,5)