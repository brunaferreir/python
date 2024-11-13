'''Exercício 6:

6. Controle de Animais de Estimação
Descrição: Desenvolva uma classe AnimalDeEstimacao com
atributos para nome, espécie e idade. Inclua métodos para
alterar a idade do animal e outro para exibir as informações do
animal.'''

class animalDeEstimacao:
    def __init__(self, nome, especie, idade):
      self.nome = nome
      self.especie = especie
      self.idade = idade 

    def alterar_idade(self, idade):
        self.idade = idade 

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Especie: {self.especie}')
        print(f'Idade: {self.idade}')

a1 = animalDeEstimacao('Apolo', 'cachorro', '2 meses') 

a1.alterar_idade('3 meses')

a1.info()


          

 
