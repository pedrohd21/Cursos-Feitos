# Numero primos
valor = int(input('Digite um numero: '))
contador = 0
for c in range(1, valor + 1):
    if valor % c == 0:
        contador += 1
print(f'contador{contador}')
"""if contador == 2:
    print('O numero {valor} � primo!')
else:
    print('N�o � primo o numero {valor}')"""
