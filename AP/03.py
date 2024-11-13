''' Exercício 5: Sistema de Gestão de Pedidos de Restaurante
Desenvolva um sistema para gerenciar os pedidos em um restaurante.

**Tarefas:**
1. Crie uma classe `Pedido` com os atributos: número do pedido, itens (uma lista de pratos), status (pendente, em preparo, entregue).
2. Implemente métodos para:
   - Adicionar itens ao pedido.
   - Alterar o status do pedido conforme ele avança no processo.
   - Exibir os detalhes do pedido (número, itens e status).

**Desafio Extra:**  
- Implemente uma classe `Prato` com atributos como nome, preço e tempo de preparo. Integre essa classe na lista de itens dos pedidos.
- Adicione um método para calcular o valor total de um pedido com base nos preços dos pratos.'''

class Pedido:
   def __init__(self, numero_pedido):
      self.numero_pedido = numero_pedido
      self.itens = []
      self.status = 'pendente'
     
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







    



       


   
   


