import random
import datetime

"""
JOGO DA FORCA
"""
print('-=-' * 10)
print('BEM VINDO AO JOGO DA FORCA')
print('-=-' * 10)

print('\nVamos começar...')

DB = ['laranja', 'uva', 'pera', 'kiwi', 'banana', 'morango', 'tomate']
vidas = 5
palavra_secreta = random.choice(DB)
palavra_jogador = '*' * len(palavra_secreta)

print(palavra_jogador)
print(palavra_secreta)
while vidas >= 0:
    ...
