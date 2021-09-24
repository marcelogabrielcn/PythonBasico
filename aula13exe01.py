"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número e lhe direi se é par ou ímpar: ')
try:
    if int(num) % 2 == 0:
        print(f'O número {num} é PAR.')
    else:
        print(f'O número {num} é ÍMPAR.')

except:
    print('Não pude converter o número informado.')
