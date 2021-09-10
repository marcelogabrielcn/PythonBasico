"""
Len - Quantidade de caracteres
len é uma função do python que informa a quantidade de caracteres, só funciona com Strings
"""

user = str(input('Digite seu nome: '))
qtd_caracteres = len(user)

print(user, qtd_caracteres, type(qtd_caracteres))

# Posso usar a função len em uma condição, para checar se a senha tem 6 dígitos por exemplo
# ou até mesmo fazer somas de Strings
txt1 = 'Olá Mundo'
txt2 = 'Hello World'
print(f'A quantidade de caracteres nos dois é: {len(txt1) + len(txt2)}')
