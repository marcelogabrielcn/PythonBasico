"""
Introdução à Formatação de Strings
Podemos formatar a forma como um print será exibido, usando as F Strings.
"""

nome = 'Marcelo Gabriel'
idade = 22
peso = 72.8
altura = 1.86
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc}.')

# Podemos ainda formatar a exibição de uma variável específica
# Por exemplo a variável imc, ao imprimir está aparecendo um número enorme
# Podemos usar as formatações.
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')  # Dessa forma teremos duas casas float depois do .

# Existe outra forma de formatar um print. Porém essa acima é a mais utilizada, e visualmente mais organizada
print('{} tem {} anos'.format(nome, idade))
