_author_='Andrey Korolev'

# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2.

text = '''Английские тексты этого раздела имеют различный уровень сложности: простые (easyy), 
сложные (hard), средней (normal) сложности. Поэтому, здесь смогут найти для себя материалы 
как новички, так уже и искушенные в изучении английского языка пользователи.'''

#import string НЕ ИМПОРТИРУЕТСЯ У МЕНЯ
punct = [',', ':', '.', '(', ')']
for i in text:
    if i in punct:
        text = text.replace(i, '')

text = text.split(' ')
words = {}
for j in text:
    if j in words:
        words[j] +=1
    else:
        words[j] = 1

import pprint
pprint.pprint(words)

