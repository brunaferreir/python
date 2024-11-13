class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.itens = []
        self.status = 'Pendente'

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f'Item "{item}" adicionado ao pedido {self.numero_pedido}.')

    def alterar_status(self, novo_status):
        status_validos = ['Pendente', 'Em preparo', 'Entregue']
        if novo_status in status_validos:
            self.status = novo_status
            print(f'Status do pedido {self.numero_pedido} alterado para: {self.status}.')
        else:
            print('Status inválido!')

    def exibir_detalhes(self):
        print(f'Número do Pedido: {self.numero_pedido}')
        print(f'Itens do Pedido: {", ".join(self.itens) if self.itens else "Nenhum item adicionado"}')
        print(f'Status do Pedido: {self.status}')


# Exemplo de uso:
pedido1 = Pedido(101)

# Adicionando itens ao pedido
pedido1.adicionar_item('Pizza Margherita')
pedido1.adicionar_item('Refrigerante')

# Alterando status do pedido
pedido1.alterar_status('Em preparo')

# Exibindo detalhes do pedido
pedido1.exibir_detalhes()

# Alterando status do pedido novamente
pedido1.alterar_status('Entregue')

# Exibindo os detalhes finais
pedido1.exibir_detalhes()
