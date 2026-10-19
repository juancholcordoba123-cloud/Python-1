# 9.4 - Vehiculo y subclase Moto que sobrescribe describir()
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def describir(self):
        print(f'Vehículo de la marca {self.marca}')


class Moto(Vehiculo):
    def describir(self):
        print(f'Moto de la marca {self.marca}')


Vehiculo('Renault').describir()
Moto('Yamaha').describir()
