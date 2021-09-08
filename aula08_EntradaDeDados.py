"""
Entrada de dados
Usamos a função input para receber algum dado via teclado.
"""

input('Qual o seu nome? ')

# Essa entrada, podemos atribui-la a uma variável
nome = input('Digite seu nome: ')
print(f'Bem vindo {nome}!')

# nota1 = input('Digite a nota 1: ')
# nota2 = input('Digite a nota 2: ')
# media = (nota1 + nota2) / 2

# Dessa forma, o input recebe sempre String, mesmo que digite 10, será '10'.
# Podemos forçar com que a entrada seja um tipo de dado específico.
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))  #nota2 = float(nota2)
media = (nota1 + nota2) / 2

idade = int(input('Digite sua idade: '))
e_maior = idade >= 18
print(f'Com {idade} anos é maior? {e_maior}')
