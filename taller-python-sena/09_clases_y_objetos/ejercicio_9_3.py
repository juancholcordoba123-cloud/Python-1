# 9.3 - Cuenta con método retirar que no permite saldo negativo
class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        if valor > self.saldo:
            print('Fondos insuficientes')
        else:
            self.saldo -= valor


c = Cuenta(1000)
c.depositar(500)
c.retirar(300)
print(c.saldo)   # 1200
c.retirar(5000)  # Fondos insuficientes
print(c.saldo)   # 1200
