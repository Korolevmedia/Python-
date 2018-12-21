_author_='Andrey Korolev'
# Пользователь вводит n и m и нужно вывести на экран:
# AAABBBAAABBBAAABBB
# BBBAAABBBAAABBBAAA
# AAABBBAAABBBAAABBB
# Для этого примера n ==3, m == 3
# где n - это количество строк, m - это кол-во троек ААА в одной строке


q = int(input('Enter any number of strings - "n": '))
f = int(input('Enter any number of letters "AAA" in single string - "m": '))

a = 'AAA'
b = 'BBB'

for i in range(q):
    c = (a + b) * f
    a, b = b, a
    print(c)

