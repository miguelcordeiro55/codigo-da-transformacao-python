# banco.py

class SaldoInsuficienteErro(Exception):
    pass


class ContaBancaria:
    def _init_(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteErro("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        return self.saldo