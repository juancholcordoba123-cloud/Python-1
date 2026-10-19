# 6.4 - Promedio de tres notas y si aprueba (3.0 o más)
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
promedio = (n1 + n2 + n3) / 3

print(f'Promedio: {promedio:.2f}')
if promedio >= 3.0:
    print('Aprueba')
else:
    print('No aprueba')
