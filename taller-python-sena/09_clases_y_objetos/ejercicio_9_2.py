# 9.2 - Clase Rectangulo con area() y perimetro()
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


r = Rectangulo(8, 5)
print('Área:', r.area())
print('Perímetro:', r.perimetro())
