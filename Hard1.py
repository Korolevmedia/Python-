_author_='Andrey Korolev'
# Пользователь вводит число определите, является ли данное число простым.
# Делится только на себя и на единицу


q = int(input('Enter any integer number: '))

if q % 2 == 0 and q != 2 or q % 3 == 0 and q != 3 or q % 5 == 0 and q != 5 or q % 7 == 0 and q != 7:
    print('Составное число')
else:
    print('Простое число')
