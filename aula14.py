"""
Formatando valores

:s - String (str)
:d - Inteiros (int)
:f - Float (float)
:.(nº)f - Quantidade de casas decimais. Ex. :.2f
:(caractere) (>, <, ^) (quantidade) (tipo - s, d, f)
"""

n_quebrado = 10/3
print(n_quebrado)
print(f'{n_quebrado:.2f}')

n1 = 1
print(f'{n1:0>10}')  # O número será formatado com 10 casas a esquerda, preenchendo com 0
n2 = 1125
print(f'{n2:0>10}')
print(f'{n2:e<10}')
print(f'{n2:e^10}')

# Posso também combinar essas formatações
print(f'{n2:0^20.10f}')

titulo = 'PYTHON'
print(f'{titulo:^50}')  # Se deixar em branco ele apenas coloca o texto centralizado
