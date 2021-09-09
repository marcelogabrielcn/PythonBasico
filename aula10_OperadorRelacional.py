"""
Operadores Relacionais - == > < >= <= !=
Trata-se de comparações entre códigos.
== - É o igual em Python
>  Maior
<  Menor
>= Maior ou igual
<= Menor ou igual
!= Diferente
"""

n1 = 10
n2 = 5*2
resultado = (n1 == n2)
print(resultado)

idade = 17
if idade > 18:
    print('Maior de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('É menor de idade')
