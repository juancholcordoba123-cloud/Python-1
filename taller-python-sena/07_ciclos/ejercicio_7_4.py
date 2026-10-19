# 7.4 - Pedir una clave con while hasta que sea la correcta
CLAVE = 'python123'

intento = input('Clave: ')
while intento != CLAVE:
    print('Clave incorrecta, intenta de nuevo')
    intento = input('Clave: ')

print('Acceso concedido')
