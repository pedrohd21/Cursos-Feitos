lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('É um triangulo', end=' ')
    if lado1 == lado2 == lado3:
        print('Equilátero!!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isósceles!!')
    else:
        print('Escaleno!!')
else:
    print('Tringulo!!')
