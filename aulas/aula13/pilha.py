# Exceções Personalizadas
class PilhaCheiaError(Exception):
    pass

class PilhaVaziaError(Exception):
    pass

# Pilha (LIFO - Last In / First Out)
class Pilha:
    def __init__(self, tamanho):
        self.__itens = tamanho * [None]
        self.__topo = -1

    def __repr__(self):
        s = ''
        for item in reversed(self.__itens[:self.__topo+1]):
            s += str(item) + '\n'
        s += f'\nTopo = {self.__topo}'
        return s

    def vazia(self):
        return self.__topo == -1

    def cheia(self):
        return self.__topo == len(self.__itens) - 1

    def empilha(self, valor):
        if self.cheia():
            raise PilhaCheiaError('Operação inválida! A pilha está cheia.')
        self.__topo += 1
        self.__itens[self.__topo] = valor

    def desempilha(self):
        if self.vazia():
            raise PilhaVaziaError('Operação inválida! A pilha está vazia.')
        item = self.__itens[self.__topo]
        self.__topo -= 1
        return item

    def destroi(self):
        self.__topo = -1

# Exemplo de uso com tratamento de exceções

pilha = Pilha(3)

try:
    pilha.empilha(10)
    pilha.empilha(20)
    pilha.empilha(30)
    pilha.empilha(40)  # Vai causar a exceção PilhaCheiaError
except PilhaCheiaError as e:
    print(f"Erro: {e}")

try:
    pilha.desempilha()
    pilha.desempilha()
    pilha.desempilha()
    pilha.desempilha()  # Vai causar a exceção PilhaVaziaError
except PilhaVaziaError as e:
    print(f"Erro: {e}")