'''  Crie uma classe chamada Retângulo que represente um retângulo. A classe deve possuir atributos para largura e altura, além de métodos para:

Calcular a área do retângulo.
Calcular o perímetro do retângulo.
Redimensionar o retângulo, alterando sua largura e altura.
Exibir as propriedades (largura e altura) do retângulo.

Implemente a classe e teste suas funcionalidades instanciando objetos e chamando seus métodos. 
'''
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura 
        self.altura = altura
    def calcularArea(self):
        return self.largura * self.altura   
    def calcularPerimentro(self):
        return 2 * (self.largura + self.altura)
    def exibir_propriedade(self):
        print(f"Largura: {self.largura}, Altura: {self.altura}")
    def redimencionar(self, nova_largura, nova_altura):
        self.largura = nova_largura
        self.altura = nova_altura    

retangulo = Retangulo(5, 10)
retangulo.exibir_propriedade()

print(f"Area: {retangulo.calcularArea()}")
print(f"Perimentro: {retangulo.calcularPerimentro()}")

retangulo.redimencionar(10, 20)
retangulo.exibir_propriedade()

print(f"Area: {retangulo.calcularArea()}")
print(f"Perimentro: {retangulo.calcularPerimentro()}")
