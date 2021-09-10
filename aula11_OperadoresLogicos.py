"""
Operadores Lógicos
AND; OR; NOT; IN; NOT IN
"""

# and (e) retorna True se todas es expressões forem verdadeiras.
print(19 > 6 and 18 < 90)

# or (ou) retorna True se uma ou outra expressão for verdadeira
print(18 > 3 or 18 > 90)

# not (não) é o inversor.
a = 2
b = 3
if b > a:
    print('B maior que A')

if not b > a:
    print('A maior que B')

# Posso usar o not para checar se uma variável está vazia
a = ''
b = 0
if not a:
    print('Por favor, preencha o valor de A')
if not b:
    print('Por favor, preencha o valor de B')

# in (em) serve para varrer uma variável, lista, tupla, etc...
nome = 'Marcelo Gabriel'
if 'M' in nome:  # Se tiver a String 'M' no nome então:
    print('Tem a letra M no nome.')

# Not in é apenas a negação
if 'L' not in nome:
    print('Não tem a letra "L" no nome')
