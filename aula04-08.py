'''Exercício 8:

8. Conta Bancária Simplificada
Descrição: Crie uma classe ContaBancaria com atributos para o
titular da conta, número da conta e saldo. Inclua métodos para
depositar e sacar dinheiro, além de um método para exibir as
informações da conta.'''

class ContaBancaria:
    def __init__(self, titular, numeroConta, saldo):
        self.titular = titular
        self.numeroConta = numeroConta
        self.saldo = saldo

    def depositar(self, saldo):
        self.saldo += saldo

    def sacar(self, saldo):
         if self.saldo >= saldo:
            self.saldo -= saldo

    def info(self):
        print(f'Titular: {self.titular}')
        print(f'Numero da Conta: {self.numeroConta}')
        print(f'Saldo: {self.saldo}')

cb =  ContaBancaria('Bruna Ferreira', '23456', 300)

cb.depositar(100)
cb.sacar(10)

cb.info()






