# 10.4 - Contar cuántas veces aparece cada palabra en una frase
frase = 'el gato y el perro juegan con el balon'
conteo = {}
for palabra in frase.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)
