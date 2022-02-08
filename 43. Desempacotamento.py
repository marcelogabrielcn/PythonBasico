"""
Desempacotamento de listas
"""

lista = ['Marcelo', 'Gabriel', 'Ferreira', 22, 1999, 9813, 13, 125]

# v1, v2, v3 = lista  # Vai dar erro porque a lista tem mais do que 3 indices
v1, v2, v3, *restante_lista = lista
print(v1, v2, v3, restante_lista)

    *restante_lista2, v1 = lista
    print(v1)

    primeiro, *restante, ultimo = lista
    print(primeiro, ultimo)

    nome, sobrenome, *_ = lista
    print(nome, sobrenome)
