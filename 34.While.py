"""

A estrutura While serve para criar um laço de repetição.
While em inglês significa enquanto. Portanto, a estrutura quer dizer,
enquanto tal condição for verdadeira, faça tal coisa.

"""

x = 0
while x < 6:
    y = 0
    while y < 6:
        print(f'({x}, {y})')
        y += 1
    x += 1
print('fim')
