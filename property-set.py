# PROPERTY / SETTER

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura  # Chama o metodo largura.setter
        self.altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self,valor):
        if valor > 0:
            self._largura = valor
        else:
            print("A largura deve ser maior que zero.")       

    @property
    def altura(self):
        return self._altura

    @altura.setter #Setter apenas recebem um valor 
    def altura(self, valor):
        if valor > 0:
            self._altura = valor    
        else:    
            print("A altura deve ser maior que zero.")

    @property
    def area(self):
        return self._largura * self._altura        

# Exemplo de uso
retangulo = Retangulo(5,10)
print(retangulo.area) #Saida 50 chama como atributo

retangulo.largura = 7
print(retangulo.area) #Saida 70

print(retangulo.altura) #Saida 10

retangulo.altura = -3  # A altura deve ser maior que 0

retangulo2 = Retangulo(-5, 10) #A largura deve ser maior que 0  não cria a variavel largura