'''Crie uma classe Cliente com os atributos: nome, telefone, endereço e histórico de pedidos (uma lista de objetos da classe Pedido).
Modifique a classe Pedido para incluir um atributo cliente que seja uma instância da classe Cliente.
Implemente métodos para:
Cadastrar um novo cliente.
Consultar o histórico de pedidos de um cliente.
Gerar relatórios com informações sobre os clientes mais frequentes.
'''
class Pedido:
    def __init__(self, numero, itens, status, cliente):
        self.numero = numero
        self.itens = itens
        self.status = status
        self.cliente = cliente

    def __str__(self):
        return f"Pedido {self.numero}: {self.status}. Cliente: {self.cliente.nome}"

class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.historico_pedidos = []

    def adicionar_pedido(self, pedido):
        self.historico_pedidos.append(pedido)

    def consultar_historico(self):
        for pedido in self.historico_pedidos:
            print(pedido)

def cadastrar_cliente(clientes):
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    novo_cliente = Cliente(nome, telefone, endereco)
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")

def consultar_historico_cliente(clientes, nome_cliente):
    for cliente in clientes:
        if cliente.nome == nome_cliente:
            cliente.consultar_historico()
            return
    print("Cliente não encontrado.")


# Exemplo de uso:
clientes = []

# Cadastrar alguns clientes
cadastrar_cliente(clientes)
cadastrar_cliente(clientes)

# Criar alguns pedidos
cliente1 = clientes[0]
pedido1 = Pedido(1, ["Pizza", "Refrigerante"], "Entregue", cliente1)
cliente1.adicionar_pedido(pedido1)

# Consultar o histórico de pedidos de um cliente
consultar_historico_cliente(clientes, cliente1.nome)
