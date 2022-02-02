"""
Split Join e Enumerate em python
"""

frase = "Você é o seu único limite!"
frase2 = frase.split(' ')
print(frase)
print(frase2)

frase3 = ' '.join(frase2)
print(frase3)

querer = 'eu vejo, eu quero, eu posso, eu pego.'
querer = querer.split(' ')
for valor in querer:
    print(f'A palavra {valor} apareceu {querer.count(valor)}x nesta frase.')

variavel_min = 'alpha'
print(variavel_min)
print(variavel_min.capitalize())

variavel_espacada = '    My name is Marcelo        '
print(variavel_espacada)
print(variavel_espacada.strip())

