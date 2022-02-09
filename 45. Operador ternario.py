"""
Operador ternário em Python
"""

logged_user = True
if logged_user:
    print('Usuário on-line')
else:
    print('Usuário off-line')

logged_admin = False
msg2 = 'Admin online' if logged_admin else 'Admin offline'
print(msg2)
