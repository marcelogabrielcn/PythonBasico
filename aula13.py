"""
Pass e Ellipsis como placeholders

Pass server como um comando de passe livre, geralmente é usado quando o dev quer colocar algo depois.
Ellipsis são os ... que tem a mesma função do pass.
"""

# PASS
valor = True
if valor:
    ...
    # Aqui era pra ter um comando, porém se eu deixar em branco, da erro na execução
else:
    print('Bye')

# Pasa isso usamos o Pass, para dizer ao código continuar, passe por esse bloco.

value = True
if value:
    pass
else:
    print('Hello!')

if value == 0:
    ...
else:
    print('Different')
