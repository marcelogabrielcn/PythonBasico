"""
Condições - IF, ELIF, ELSE
A condição IF (se), implica em uma determinada condição para executar uma parte do código
ELIF é Se não, se ... vem uma outra condição
ELSE é o senão. Condição final caso as outras forem falsas.
"""

if True:
    print('Verdade')
print('Expressão falsa')

# Por ser uma parte exclusiva do código, temos um 'bloco' separado
# Tudo que esta dentro desse bloco faz parte da condição.
# Podemos definir o que esta dentro com 4 espaços, ou TAB.

opt = False
if opt:
    print('É verdade')
else:
    print('Não é verdadeiro.')

# Se opt for True, executa a primeira parte, se não, a segunda.
# Posso ter várias condições dentro de uma condição

if opt:
    print('1a condição')
    if True:
        print('2a condição')

# Ao fazer várias condições é preciso se atentar muito bem a hierarquia do código e edentação.
