"""
For in
"""

texto = 'Você é o seu único limite!'
novo_texto = ''

for letra in texto:
    if letra in 'aeiou':
        novo_texto += letra.upper()
    else:
        novo_texto += letra
print(f'O novo texto agora é: {novo_texto}')
