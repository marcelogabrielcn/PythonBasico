"""
Enumerate - Enumerar elementos da lista
"""

listaMae = [
    ['Lucas', 'João', 'Daniel'],
    ['Ana', 'Julia', 'Yasmin'],
    ['Thais', 'Thaina', 'Thami']
]
print(listaMae[0][0])
print(listaMae[2][0])
print(listaMae[0])

listCopy = list(enumerate(listaMae))
print(listCopy)
print(listCopy[0])
print(listCopy[0][0])
print(listCopy[2][1][0])

for v1, v2 in enumerate(listaMae):
    print(v1, v2)

for v1, v2 in enumerate(listaMae, 47):
    print(v1, v2)

for v1 in enumerate(listaMae):
    print(v1)
    valor_num, lista_nomes = v1
    print(valor_num)
    print(lista_nomes)
    nome1, nome2, nome3 = lista_nomes
    print(nome1)
    