class Conta:
    def __init__(self, nomeCliente, numConta, tipoInterese, saldo):
        self.nomeCliente = nomeCliente
        self.numConta = numConta
        self.tipoInterese = tipoInterese
        self.saldo = saldo

    def get_nomeCliente(self):
        return self.__nomeCliente

    def set_nomeCliente(self, nome):
        self.__nomeCliente = nome

    def get_numConta(self):
        return self.__numConta

    def set_numConta(self, num):
        self.__numConta = num

    def get_tipoInterese(self):
        return self.__tipoInterese

    def set_tipoInterese(self, tipoInterese):
        self.__tipoInterese = tipoInterese

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    nomeCliente = property(get_nomeCliente, set_nomeCliente)
    numConta = property(get_numConta, set_numConta)
    tipoInterese = property(get_tipoInterese, set_tipoInterese)
    saldo = property(get_saldo, set_saldo)

    def metodosIngreso (self, aumento):
        if aumento > 0:
            self.saldo += aumento
        else:
            return 0

    def reintegro(self, cantidade):
        if cantidade > 0:
            self.saldo -= cantidade
        else:
            return 0

    def contaOrixe(self, contaDestino, importe):
        if importe > 0 and self.saldo >= importe:
            self.reintegro(importe)
            contaDestino.metodosIngreso(importe)
            print(f"Transferencia de {importe} realizada")
        else:
            print(f"Transferencia non realizada. Saldo insuficiente")


conta1 = Conta("Hugo", 1234, 21, 1500)
conta2 = Conta("Jose", 4321, 10, 750)

conta1.contaOrixe(conta2, 500)

print("O saldo da conta1 é:", conta1.saldo)
print("O saldo da conta2 é:", conta2.saldo)

