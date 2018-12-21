_author_='Andrey Korolev'
# Найдите n-ое число Фибоначчи


q = int(input('Enter any ordinal number of Fibonacci number: '))

a = 1
b = 0
i = 0
for i in range(q):
    fib = a + b
    a = b
    b = fib
print(fib)


