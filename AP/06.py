class Pedido:
    def __init__(self, numero, items, status, cliente):
        self.numero = numero
        self.items = items
        self.status = status
        self.cliente = cliente

    def __str__(self):
         return f"Pedido {self.numero}: {self.status}. Cliente: {self.cliente.nome}"
    
    