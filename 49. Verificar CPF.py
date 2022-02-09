"""
Desafio - Validar CPF
"""

cpf = str(input("Digite seu CPF: ")).strip()
novo_cpf = cpf.replace('.', '').replace('-', '')

# Verificar 1o digito
mult = 10
soma = 0

for num in novo_cpf:
    if mult >= 2:
        res = int(num) * mult
        soma += res
        mult -= 1

d1 = 11 - (soma % 11)
if d1 > 9:
    d1 = 0

# Verificar 2o digito
mult2 = 11
soma2 = 0

for num in novo_cpf:
    if mult2 >= 2:
        res2 = int(num) * mult2
        soma2 += res2
        mult2 -= 1

d2 = 11 - (soma2 % 11)
if d2 > 9:
    d2 = 0

if d1 == int(novo_cpf[9]) and d2 == int(novo_cpf[10]):
    print('CPF Válido!')
    print(novo_cpf[0:3], novo_cpf[3:6], novo_cpf[6:9], sep='.', end='-')
    print(novo_cpf[9:11])
else:
    print('Oops, CPF inválido')

print(novo_cpf[0:3], novo_cpf[3:6], novo_cpf[6:9], sep='.', end='-')
print(novo_cpf[9:11])

print(soma, soma2)
print(d1, d2)
print(novo_cpf[9], novo_cpf[10])
