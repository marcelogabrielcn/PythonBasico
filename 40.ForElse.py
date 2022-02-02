"""
For / Else em python
.startswith()
.lower()
"""
letra_o = 0

palavra = 'Notebook'
for letra in palavra:
    print(letra)
    if letra == 'o':
        letra_o += 1
print(f'Tem {letra_o} letras "o"')

lista = ['uva', 'banana', 'melancia']

for frutas in lista:
    if len(frutas) == 6:
        print(frutas)
    else:
        print('Estude sempre!')

print('Fim da parte 01')

for frutas in lista:
    if frutas.lower().startswith('b'):
        print('Opa, tem uma fruta que começa com B')
    else:
        print(frutas)

print(palavra)
palavra_min = palavra.lower()
print(palavra_min)
