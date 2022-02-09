"""
Expressão condiocinal com operador OR
"""

nome = str(input('Qual o seu nome? '))
if nome:
    print(f'Olá {nome}.')
else:
    print('Oops você não digitou nada.')

nome2 = str(input('Qual o seu nome? '))
print(nome2 or 'Oops, acho que você não digitou nada.')
