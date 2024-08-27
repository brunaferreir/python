class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar(self, qtde):
        self.quantidade += qtde

    def remover(self, qtde):
        if self.quantidade >= qtde:
            self.quantidade -= qtde
        else:
            print('Quantidade insuficiente!!!')

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.quantidade}')