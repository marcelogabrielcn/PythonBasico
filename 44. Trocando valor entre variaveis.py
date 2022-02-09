"""
Trocando o valor entre variáveis em Python
"""

x = 10
y = 'Python'
z = x
x = y
y = z
print(f'X = {x}, Y = {y}')

a = 22
b = 'Marcelo'
c = 'São Paulo'
d = 'Desenvolvedor'
a, b, c, d = d, b, c, a
print(f'A = {a}, B = {b}, C = {c}, D = {d}')
