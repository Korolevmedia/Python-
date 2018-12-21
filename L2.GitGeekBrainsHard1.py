_author_='Andrey Korolev'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5

a = float(equation[4:7])
z = float(equation[11:24])
y = a * x + z
print(y)



