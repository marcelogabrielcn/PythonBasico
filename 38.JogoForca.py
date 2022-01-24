import random
from time import sleep

"""
JOGO DA FORCA
"""
print('-=-' * 10)
print('BEM VINDO AO JOGO DA FORCA')
print('-=-' * 10)

print('\nVamos começar...')
sleep(1)
print('Dica: A palavra secréta é uma fruta...')
sleep(2)

DB = ['laranja', 'uva', 'pera', 'kiwi', 'banana', 'morango', 'tomate', 'melancia']
vidas = 5
palavra_secreta = random.choice(DB)
print(f'A palavra secreta tem {len(palavra_secreta)} letras.')
sleep(1.5)

print(palavra_secreta)
letras_digitadas = []
while True:
    if vidas > 0:
        print(f'Você tem {vidas} tentativas')
        palavra_temporaria = ''

        letra_jogador = str(input('Digite uma letra: '))

        for letras in palavra_secreta:
            if letra_jogador in palavra_secreta:
                letras_digitadas.append(letra_jogador)

            else:
                palavra_temporaria += '*'
        print(palavra_temporaria)
