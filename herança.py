# HERANÇA Aula 06
# classe mãe(superclasse):
class veiculo:
    def __init__ (self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

# classe filha (subclasse)
class carro(veiculo):
    def __init__ (self, marca, modelo, placa, portas):
# incluindo atributos específicos do carro        
        super().__init__(marca, modelo, placa)
        self.portas = portas

# Criando um método exibir

    def exibir(self):
        print('-------------------------')
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Placa: ', self.placa)
        print('Portas: ', self.portas)
        

class moto(veiculo):
    def __init__ (self, marca, modelo, placa, cor):
        super().__init__(marca, modelo, placa)
        self.cor = cor

    def exibir(self):
        print('-------------------------')
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Placa: ', self.placa)
        print('Cor: ', self.cor)
        

carro1 = carro('Honda', 'Civic', 'GAY-2411', 4)
carro1.exibir()
moto1 = moto('Harley', 'Davidson 883', 'XXT-2269', 'Preto' )
moto1.exibir()
