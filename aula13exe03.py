"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos,
escreva: Seu nome é curto, se tiver entre 5 e 6 letras: seu nome pe normal,
se tiver mais que 6 letras: seu nome é muito grande.
"""

nome = str(input('Type your name: '))
qtd_nome = len(nome)
if qtd_nome <= 4:
    print(f'Olá {nome}, seu nome possui apenas {qtd_nome} letras, e é muito curto.')
elif qtd_nome <= 6:
    print(f'Olá {nome}, seu nome possui {qtd_nome} letras, e é normal.')
else:
    print(f'Olá {nome}, seu nome possui {qtd_nome} letras, e é muito grande.')
