"""
Tipos primitivos de dados
str - String                    'frases' "Assim"
int - Inteiro                   1234  -143   0
float - Real/ponto flutuante    10.6  19.02  -24.9243  (usa ponto . não virgula ,)
bool - Booleano/lógico          True/False
"""
# Existem outros tipos primitivos, mas esses são os principais.

# Para saber o tipo de dado, podemos usar o parâmetro 'type'

print('Marcelo', type('Marcelo'))
print(1999, type(1999))
print(185.65, type(185.65))
print(10 == 10, type(10 == 10))


# Podemos também converter os tipos de dados.

print('50', type('50'), type(int('50')))  # Desta forma com a função int, converti o '50' em inteiro.
print("", type(""), type(bool("")))
print(bool(""))

# Nesta linha acima, o tipo bool("") vai dar false, pois esta vazio, vamos usar isso futuramente em condições.





