# 6.3 - Saludo según la hora (0 a 23)
hora = int(input('Hora (0-23): '))
if 0 <= hora < 12:
    print('Buenos días')
elif 12 <= hora < 18:
    print('Buenas tardes')
elif 18 <= hora <= 23:
    print('Buenas noches')
else:
    print('Hora no válida')
