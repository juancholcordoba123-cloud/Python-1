# 12.3 - Lee registro.txt línea por línea (ejecutar después del 12.2)
try:
    with open('registro.txt', 'r', encoding='utf-8') as f:
        for linea in f:
            print(linea.strip())
except FileNotFoundError:
    print('Primero ejecuta ejercicio_12_2.py para crear registro.txt')
