# 9.1 - Clase Aprendiz con nombre y ficha
class Aprendiz:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def mostrar(self):
        print(f'Aprendiz: {self.nombre} | Ficha: {self.ficha}')


a = Aprendiz('Juan Pérez', '2567890')
a.mostrar()
