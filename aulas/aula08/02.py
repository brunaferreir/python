class Animal:
    def __init__ (self, nome, cor, numeroPatas):
        self.nome = nome
        self.cor = cor
        self.numeroPatas = numeroPatas

    def exibir_dados(self):
     print("Nome:",self.nome)  
     print("Cor:",self.cor)
     print("Numero de Patas:",self.numeroPatas)
     


class Cachorro(Animal):
   def __init__(self, nome, cor, numeroPatas, raca):
      super().__init__(nome, cor, numeroPatas)
      self.raca = raca

   def exibir_dados(self):
     print("Nome:",self.nome)  
     print("Cor:",self.cor)
     print("Numero de Patas:",self.numeroPatas)
     print("Raca:",self.raca)

    

animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados() # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados() # exibe os atributos do cachorro      

    
       