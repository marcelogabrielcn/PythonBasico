"""
36. Iterando Strings com while
"""

frase = 'O girassol, gira conforme o sol'
tam_frase = len(frase)
contador = 0
nova_frase = ''

letra_mai = str(input('Qual letra deseja deixar maiúscula?')).lower()

while contador < tam_frase:
    print(frase[contador], contador)

    letra = frase[contador]
    if letra == letra_mai:
        nova_frase += letra.upper()
    else:
        nova_frase += letra

    contador += 1

print(f'\n{nova_frase}')
