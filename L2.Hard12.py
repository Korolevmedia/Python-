_author_='Andrey Korolev'

# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1.
# 2. Сколько букв английского алфавита в тексте?


text = '''Английские тексты этого раздела имеют различный уровень сложности: простые (easyy),
          сложные (hard), средней (normal) сложности. Поэтому, здесь смогут найти для себя материалы
          как новички, так уже и искушенные в изучении английского языка пользователи.'''
english = ['a','b','c','d','e','f','g','h','j','i','k','l','m','n','o','p','r','t','y','u','q','w','s','z','x','v']

#import string НЕ ИМПОРТИРУЕТСЯ У МЕНЯ
punct = [',', ':', '.', '(', ')', ' ']
for i in text:
    if i in punct:
        text = text.replace(i, '')

text = text.lower()
letters = []
for k in text:
    if k in english:
        letters.append(k)

letters_statistics = {}
for j in letters:
    if j in letters_statistics:
        letters_statistics[j] +=1
    else:
        letters_statistics[j] = 1

import pprint
pprint.pprint(letters_statistics)
