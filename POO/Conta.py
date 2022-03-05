class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transferirvalor(self, contadestino, valor):
        if self.saldo < valor:
           return print('Saldo insuficiente')
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            return print('Tranferencia realizada com sucesso!')

conta = Conta()







