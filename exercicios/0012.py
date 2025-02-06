''' Exercício 1: Classe Círculo
Crie uma classe chamada Círculo que represente um círculo. A classe deve ter os seguintes atributos:

raio: O raio do círculo.
A classe deve ter os seguintes métodos:

__init__(self, raio): O construtor da classe, que inicializa o raio do círculo.
calcular_area(self): Um método que calcula e retorna a área do círculo.
calcular_circunferencia(self): Um método que calcula e retorna a circunferência do círculo.
exibir_propriedades(self): Um método que exibe o raio, a área e a circunferência do círculo.

'''

class Circulo:
    def __init__ (self, raio):
        self.raio = raio
    def calcularArea(self):
        return 3.14 * self.raio ** 2
    
    def calcularCircuferencia(self):
        return (2 * self.raio) * 3.14 
    
    def exibirPropriendades(self):
        print(f"Raio: {self.raio}")
        print(f"Area: {circulo.calcularArea()}")
        print(f"Circuferencia: {circulo.calcularCircuferencia()}")

    def redimencionar(self, nova_area):
        self.area = nova_area  

circulo = Circulo(5)

circulo.exibirPropriendades()

circulo.redimencionar(7)
circulo.exibirPropriendades()