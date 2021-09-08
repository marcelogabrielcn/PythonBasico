"""
Criar variáveis para nome (str), idade(int)
altura (float) e peso(float) de uma pessoa
Criar variável com ano atual (int)
Obter o ano de nascimento da pessoa (com base na idade e ano atual)
Obter o IMC da pessoa, imprimir com duas casas decimais
Exibir um texto formatado com todos os valores, usando F-Strings
"""

nome = 'Marcelo'
idade = 22
altura = 1.86
peso = 72.80
ano_atual = 2021
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é: {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')
