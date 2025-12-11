class Coche:
    def __init__(self):
        self.velocidade = 0

    def getVelocidade(self):
        return self.velocidade

    def acelerar(self, valor):
        if valor > 0:
            self.velocidade += valor

    def frenar(self, menos):
        if menos > 0:
            self.velocidade -= menos


class Boletin9_3(Coche):
    def __init__(self):
        super().__init__()

    def prueba(self):
        print("Velocidad inicial:", self.getVelocidade())
        self.acelerar(50)
        print("Velocidad después de acelerar:", self.getVelocidade())
        self.frenar(20)
        print("Velocidad después de frenar:", self.getVelocidade())



if __name__ == "__main__":
    boletin = Boletin9_3()
    boletin.prueba()