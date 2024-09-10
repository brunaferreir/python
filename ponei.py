class ponei:
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self):
        self.vida = self.vida - self.ataque
        

    def fugir(self):
        print("Você fugiu")

class pegasus(ponei):
    def __init__(self, vida, ataque, defesa, asa):
        super().__init__(vida, ataque, defesa)
        self.asa = asa
    def voar(self):
        pass
        
    def exibir(self):
        print('-------------------------')
        print('Vida: ', self.vida)
        print('Ataque: ', self.ataque)
        print('Defesa: ', self.defesa)
        print('Asa: ', self.asa)

class unicornio(ponei):
    def __init__(self, vida, ataque, defesa, chifre):
        super().__init__(vida, ataque, defesa)
        self.chifre = chifre
    def magia(self):
        pass

    def exibir(self):
        print('-------------------------')
        print('Vida: ', self.vida)
        print('Ataque: ', self.ataque)
        print('Defesa: ', self.defesa)
        print('Chifre: ', self.chifre)

ponei1 = pegasus(200, 25, 15, 'Roxa')
ponei2 = unicornio(200, 50, 20, 'Verde')
ponei2.atacar()
ponei1.atacar()
ponei2.exibir()
ponei1.exibir()
ponei2.fugir()
