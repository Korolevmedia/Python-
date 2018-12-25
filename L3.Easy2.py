_author_='Andrey Korolev'

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    n = str(ticket_number)
    first3digits = int(n[0]) + int(n[1]) + int(n[2])
    last3digits = int(n[-1]) + int(n[-2]) + int(n[-3])
    if first3digits == last3digits:
        return True
    else:
        return False

ticket_number = 456375
print('Is it a lucky ticket?' , lucky_ticket(ticket_number))