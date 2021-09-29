"""
Faça um programa que pergunte ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex. Bom dia (0-11h), boa tarde, boa noite.
"""

try:
    hora = int(input('Informe que horas são, sem os minutos: '))
    if 4 <= hora <= 12:
        print('Olá, bom dia!')
    elif 13 <= hora <= 18:
        print('Olá, boa tarde.')
    else:
        print('Oi, boa noite.')

except:
    print('Não consegui entender as horas.')
