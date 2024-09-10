class passaro: #Classe mae superclasse
    def __init__ (self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        pass

    def fugir(self, destino):
        pass

class passaroAereo(passaro): #Classe filha subclasse da classe passaro
    def voar(self):
      pass

    def exibir(self):
        print('-------------------------')
        print('Vida: ', self.vida)
        print('Ataque: ', self.ataque)
        print('Defesa: ', self.defesa)
        print('Companheiro: ', self.companheiro)   

class passaroAquatico(passaro):    
    def nadar(self):
      pass

    def exibir(self):
        print('-------------------------')
        print('Vida: ', self.vida)
        print('Ataque: ', self.ataque)
        print('Defesa: ', self.defesa)
        print('Peso: ', self.peso)
      

class passaroCompanhia(passaroAereo):
    def __init__(self, vida, ataque, defesa, companheiro): #Atribuindo uma especialização "COMPANHEIRO"
        self.companheiro = companheiro
        super().__init__(vida, ataque, defesa)


class Pinguim(passaroAquatico):
    def __init__(self, vida, ataque, defesa, peso): #Atribuindo uma especialização "PESO"
        self.peso = peso
        super().__init__(vida, ataque, defesa)

#  Criação de objetos
aguia = passaroCompanhia(100, 300, 250, 'Rafael')   
pinguim = Pinguim(140, 80, 400, 5)   


aguia.exibir()
pinguim.exibir()

