'''Exercício 1: Básico de Membros Públicos e Privados

Crie uma classe ContaBancaria que tenha um atributo
privado saldo e um atributo público titular. Inicialize ambos
os atributos no método __init__. Em seguida, crie um método
para depositar dinheiro e outro para exibir o saldo, garantindo
que o saldo não possa ser acessado diretamente de fora da
classe.'''

class ContaBancaria:
    def __init__(self):
        self.titular = "Bruna"
        self.__saldo = 300 
 
    def depositar(self, __saldo):
         self.__saldo += __saldo

    def __exibir(self):
        return self.__saldo
      
       

conta = ContaBancaria()

print(conta.titular)

conta.depositar(100 + 20)

print(conta._ContaBancaria__exibir())


