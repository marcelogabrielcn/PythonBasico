"""
Listas em Python
"""

lista = []
lista.append(1)
lista.append('Marcelo Gabriel')
lista.append(10.24)
lista.insert(0, False)

print(lista)
print(lista[0:2])

lista.pop(1)
print(lista)

del lista[0:2]

print(lista)
lista.clear()
print(lista)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l2.extend(l1)
print(l2)

l3 = l1 + l2
print(l3)

print(min(l3))
print(max(l3))

l4 = [*range(0,10,2)]
print(l4)
