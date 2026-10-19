# 11.2 - Lanzar un dado 5 veces con random
from random import randint

for i in range(5):
    print(f'Lanzamiento {i + 1}: {randint(1, 6)}')
