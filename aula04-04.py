'''Exercício 4:

4. Veículo
Descrição: Implemente uma classe Carro com atributos para
marca, modelo, ano e quilometragem. Inclua métodos para
dirigir o carro, que aumenta a quilometragem, e outro método
para exibir informações do carro.'''

class Carro:
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def velocidade(self, quilometragem):
        self.quilometragem += quilometragem

    def info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Quilometragem: {self.quilometragem}')

v1 = Carro('Chevrolet', 'Tracker' , 2023 , 100)
v1.velocidade(103)
v1.info()











