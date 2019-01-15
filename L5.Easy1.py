_author_='Andrey Korolev'

# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
#dir_path = r"/Users/andreykorolev/PycharmProjects/GeekBrains/Lesson5"

a = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']

for i in a:
    if not os.path.exists(os.path.join('.', i)):
        os.mkdir(os.path.join('.', i))

b = input('Enter command:')
if b == 'delete':
    for i in a:
        os.rmdir(i)




