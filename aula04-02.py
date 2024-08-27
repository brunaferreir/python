'''Exercício 2:

2. Gerenciamento de Pessoas
Descrição: Crie uma classe Pessoa com atributos para nome,
idade e endereço. Inclua métodos para alterar o endereço e
outro para exibir todas as informações da pessoa.'''


class pessoas:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mudar_endereco(self, endereco):
        self.endereco = endereco


    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'endereço: {self.endereco}')       

p1 = pessoas('Bruna', 18, 'Rua das perolas')

p1.mudar_endereco('Rua do guardachuva')

p1.info()








