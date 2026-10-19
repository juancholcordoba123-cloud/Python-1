# 12.1 - Pide dos números y muestra suma, resta, multiplicación y división
a = float(input('Primer número: '))
b = float(input('Segundo número: '))

print(f'Suma: {a + b}')
print(f'Resta: {a - b}')
print(f'Multiplicación: {a * b}')
if b != 0:
    print(f'División: {a / b}')
else:
    print('División: no se puede dividir entre cero')
