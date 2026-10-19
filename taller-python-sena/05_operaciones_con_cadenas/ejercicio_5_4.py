# 5.4 - Invertir una cadena y verificar si es palíndromo
texto = input('Texto: ')
limpio = texto.lower().replace(' ', '')
invertido = limpio[::-1]

print('Invertido:', texto[::-1])
if limpio == invertido:
    print('Es un palíndromo')
else:
    print('No es un palíndromo')
