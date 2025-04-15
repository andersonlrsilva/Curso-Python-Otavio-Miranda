from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, num):
        self.agencia = agencia
        self.num = num
        self._saldo = 0

    @abstractmethod
    def saque(self): ...

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def deposito(self, deposito):
        self._saldo = self._saldo + deposito
        print(f'Valor depositado R$ {deposito}')


# Conta Corrente
class Corrente(Conta):
    def __init__(self, agencia, num):
        super().__init__(agencia, num)
        self.limite = 0

    def saque(self, valorsaque):
        if self.limite == 0:
            if self.saldo < valorsaque:
                print(f'Valor excede limite da conta R$ {self.limite}')

            else:
                valorfinal = (self.limite + self.saldo) - valorsaque
                self.limite = valorfinal

                print(valorfinal)
                print('Saque efetuado')


# Conta Poupança

class Poupanca(Conta):
    def __init__(self, agencia, num):
        super().__init__(agencia, num)

    def saque(self): ...


# instancia conta corrente
conta = Corrente('2133', '7079')
nome_clas = conta.__class__.__name__
print(f"Conta {nome_clas}: {conta.num} Agência: {conta.agencia}")
print()
print()
print(f'Saldo Total: {conta.saldo}')
conta.deposito = 100
conta.deposito = 501
print(f"Valor Total = R${conta.saldo},00")
print()
print()
print()
conta.saque(600)
print(f'Saldo Total: {conta.saldo}')
print()
print()


# instancia poupanca
# conta = Poupanca('2133', '8001')
# nome_clas = conta.__class__.__name__
# print (f"Conta {nome_clas}: {conta.num} Agência: {conta.agencia}")
# print()
# print()
# print(f'Saldo Total: {conta.saldo}')
# conta.deposito = 125
# conta.deposito = 485
# print(f"Valor Total = R${conta.saldo},00")
