import random
from time import sleep

"""
JOGO DA FORCA
"""
print('-=-' * 10)
print('BEM VINDO AO JOGO DA FORCA')
print('-=-' * 10)

print('\nVamos começar...')
sleep(0.5)

DB = ['laranja', 'uva', 'pera', 'kiwi', 'banana', 'morango', 'tomate']
vidas = 5
palavra_secreta = random.choice(DB)
palavra_jogador = '*' * len(palavra_secreta)


print(palavra_jogador)
print(palavra_secreta)
while vidas >= 0:
    letra = str(input('Digite uma letra: '))
    for i, l in enumerate(palavra_secreta):
        if letra == l:
            ...
        else:
            print('Oops, não tem essa letra.')
            vidas -= 1

print(palavra_secreta)
print(palavra_jogador)
