# 12.2 - Pide nombre y ficha y los guarda en registro.txt
nombre = input('Nombre del aprendiz: ')
ficha = input('Ficha: ')

with open('registro.txt', 'w', encoding='utf-8') as f:
    f.write(f'{nombre}\n')
    f.write(f'{ficha}\n')

print('Datos guardados en registro.txt')
