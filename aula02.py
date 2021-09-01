print('Marcelo', 'Gabriel')

# Por padrão o python adiciona um espaço ao imprimir duas palavras, como no exemplo acima.
# Mas podemos mudar isso, com o argumento 'sep' (separador).

print('Beija', 'flor', sep='-')
print('Arco', 'Iris', sep='*')

# Posso também mudar o que será exibido no final do print.
# Por padrão, no final do print é posto uma quebra de linha.
# Para isso temos o argumento 'end'.

print('Estou estudando Python.', end='')  # Ao deixar end='' (vazio) eu retiro a quebra de linha.
print(' Python é uma linguagem de programação.')
