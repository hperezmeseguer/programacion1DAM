class Consumo:
    def __init__(self, km = 0, litros = 0, vMed = 0, pGas = 0):
        self.km = km
        self.litros = litros
        self.vMed = vMed
        self.pGas = pGas

    def getTempo(self):
        if self.vMed > 0:
            return self.km / self.vMed
        return 0

    def consumoMedio(self):
        if self.km > 0:
            return (self.litros / self.km) * 100
        return 0

    def consumoEuros(self):
        return self.consumoMedio() * self.pGas

    def setKms(self, km):
        self.km = km

    def setLitros(self, litros):
        self.litros = litros

    def setVMed(self, vMed):
        self.vMed = vMed

    def setPGas(self, pGas):
        self.pGas = pGas


obx1 = Consumo()
obx1.setLitros(50)
obx1.setPGas(1.57)

obx2 = Consumo(100, 30, 100, 1.55)
print("Consumo medio do obx2:", obx2.consumoMedio(), "L/100 km")


obx2.setLitros(25)
print("Velocidade media do obx2:", obx2.vMed, "km/h")


