# 12.4 - Pide 3 notas, calcula el promedio y guarda Aprobó / No aprobó
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

promedio = (n1 + n2 + n3) / 3
mensaje = 'Aprobó' if promedio >= 3.0 else 'No aprobó'

with open('resultado.txt', 'w', encoding='utf-8') as f:
    f.write(f'Promedio: {promedio:.2f}\n')
    f.write(f'{mensaje}\n')

print(f'Promedio: {promedio:.2f} -> {mensaje} (guardado en resultado.txt)')
