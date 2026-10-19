# 10.1 - Diccionario con los datos de un libro
libro = {
    'título': 'Cien años de soledad',
    'autor': 'Gabriel García Márquez',
    'año': 1967,
}

for clave, valor in libro.items():
    print(f'{clave}: {valor}')
