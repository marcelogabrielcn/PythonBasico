"""
Sistema simples de verificação de login
"""

user = str(input('Nome de usuário: '))
password = str(input('Senha: '))

user_db = 'Marcelo'
password_db = '123456'

if user == user_db and password == password_db:
    print('Bem vindo ao sistema!')
else:
    print('Usuário ou senha incorretos.')
