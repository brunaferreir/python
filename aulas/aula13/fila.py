# Exceções Personalizadas
class FilaCheiaError(Exception):
    pass

class FilaVaziaError(Exception):
    pass

# Fila (FIFO - First In / First Out)
class Fila:
    def __init__(self, tamanho):
        self.__itens = tamanho * [None]
        self.__fim = 0

    def __repr__(self):
        s = 'S ⇽ |'
        for item in self.__itens[:self.__fim]:
            s += f' {item} |'
        s += ' ⇽ E'
        return s

    def vazia(self):
        return self.__fim == 0

    def cheia(self):
        return self.__fim == len(self.__itens)

    def enfileira(self, valor):
        if self.cheia():
            raise FilaCheiaError('Operação inválida! A fila está cheia.')
        self.__itens[self.__fim] = valor
        self.__fim += 1

    def desenfileira(self):
        if self.vazia():
            raise FilaVaziaError('Operação inválida! A fila está vazia.')
        item = self.__itens[0]
        for i in range(1, self.__fim):
            self.__itens[i-1] = self.__itens[i]
        self.__fim -= 1
        return item

    def destroi(self):
        self.__fim = 0

# Exemplo de uso com tratamento de exceções

fila = Fila(3)

try:
    fila.enfileira(10)
    fila.enfileira(20)
    fila.enfileira(30)
    fila.enfileira(40)  # Vai causar a exceção FilaCheiaError
except FilaCheiaError as e:
    print(f"Erro: {e}")

try:
    fila.desenfileira()
    fila.desenfileira()
    fila.desenfileira()
    fila.desenfileira()  # Vai causar a exceção FilaVaziaError
except FilaVaziaError as e:
    print(f"Erro: {e}")