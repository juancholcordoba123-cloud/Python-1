# 8.3 - Número mayor de una lista sin usar max
def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

print(mayor([4, 17, 9, 2, 15]))
