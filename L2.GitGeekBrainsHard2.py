_author_='Andrey Korolev'

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

a = input('Enter date in format "dd.mm.yyyy"  ')
b = a.split('.')
dd = b[0]
mm = b[1]
yyyy = b[2]
months31 = [1, 3, 5, 7, 8, 10, 12]
months30 = [4, 6, 9, 11]

if len(dd) == 2:
    if len(mm) == 2:
        if len(yyyy) == 4 and 1 <= int(yyyy) <= 9999:
            if 1 <= int(dd) <= 29 and 1 <= int(mm) <= 12 or int(dd) == 30 and int(mm) in months30 or int(dd) == 31 and int(mm) in months31:
                print('date format is correct')
            else:
                 print('date format is NOT correct')
        else:
            print('date format is NOT correct')
    else:
         print('date format is NOT correct')
else:
    print('date format is NOT correct')
