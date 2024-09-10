'''Exercício 2: Getters e Setters Simples

Crie uma classe Lampada com um atributo privado estado
(ligado/desligado). Implemente métodos getters e setters para o
atributo estado. O setter deve aceitar apenas os valores
"ligado" ou "desligado" e alterar o estado da lâmpada de
acordo.'''

class Lampada:
    def __init__(self, estado):
        self.set_estado(estado)

    def get_estado(self):
        return self._estado 

    def set_estado(self, novo_estado):
      if novo_estado == "Ligado":
        self._estado = novo_estado 
      elif novo_estado == "Desligado":
        self._estado = novo_estado
      else:
        self._estado = print("Valor invalido! O estado deve ser 'Ligado' ou 'Desligado'")


lampada = Lampada("Ligadsds")
print(lampada.get_estado())             


