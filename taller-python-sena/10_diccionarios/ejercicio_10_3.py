# 10.3 - Verificar si una palabra existe en un diccionario español-inglés
traducciones = {
    'casa': 'house',
    'perro': 'dog',
    'gato': 'cat',
    'libro': 'book',
}

palabra = input('Palabra en español: ').lower()
if palabra in traducciones:
    print(f'{palabra} = {traducciones[palabra]}')
else:
    print('La palabra no está en el diccionario')
