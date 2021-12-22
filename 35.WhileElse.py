"""
35. While / Else
Uso de contadores e acumuladores
"""

contador = 5
acumulador = 0

while contador <= 10:
    print(contador)

    #if contador == 7:
        #break

    acumulador += 1
    contador += 1

else:
    print('cheguei no else')

print(f'Foram ao todo {acumulador} iterações')
print('Fim do programa')
