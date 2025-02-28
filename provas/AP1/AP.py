import random

class Nim:
    def __init__(self, pedras, jogador1, jogador2=None):
        self.jogador1 = jogador1
        self.jogador2 = jogador2 if jogador2 else "Bot"
        self.pedras = pedras
        self.jogadorAtual = 1

    def exibirStatus(self):
        print(f"Ainda há {self.pedras} pedras.")
        print(f"É a vez de {self.jogador1 if self.jogadorAtual == 1 else self.jogador2}.")

    def regras(self):
        print("Regras: \nNúmero total de pedras: 21 \nO jogador pode retirar entre 1 e 3 pedras.")
        print("")

    def rodadaJogador(self):
        while True:
            valor = int(input(f"Jogador(a) {self.jogador1 if self.jogadorAtual == 1 else self.jogador2}, digite quantas pedras deseja retirar: "))
            if valor >0 and valor <= 3:
                self.pedras -= valor
                print(f"O jogador {self.jogador1 if self.jogadorAtual == 1 else self.jogador2} remove {valor} pedra(s).")
                break
            else:
                print("Valor inválido. Você pode retirar entre 1 e 3 pedras.")
            

    def rodadaBot(self):
        if self.pedras == 3:
            valor = random.randint(1,2)
        elif self.pedras == 2:
            valor = 1
        else:
            valor = random.randint(1, 3)
        print(f"Bot remove {valor} pedra(s).")
        self.pedras -= valor

    def alternarJogador(self):
        self.jogadorAtual = 2 if self.jogadorAtual == 1 else 1

    def perdedor(self):
        if self.pedras == 1:
            return True
        return False

    def jogar(self, modo):
        self.regras()
        while self.pedras > 1: 
            self.exibirStatus()

            if self.jogadorAtual == 1 or modo == 1: 
                self.rodadaJogador()
            else:  
                self.rodadaBot()

            if self.perdedor():

                if self.jogadorAtual == 1:
                    print(f"Sobrou 1 pedra. O jogador {self.jogador2} perdeu!")
                else:
                    print(f"Sobrou 1 pedra. O jogador {self.jogador1} perdeu!") 
                break

            self.alternarJogador()  

def escolherModo():
    while True: 
        print("Escolha o modo de jogo:")
        print("1. Jogador vs Jogador")
        print("2. Jogador vs Bot")
        modo = int(input("Digite 1 ou 2: "))
        if modo == 1 or modo == 2:
            return modo
        else:
            print("Escolha inválida. Tente novamente.")

def nomeJogador(num):
    nome = input(f"Digite o nome do Jogador {num}: ")
    return nome

if __name__ == "__main__":

    modo = escolherModo()

    if modo == 1: 
        jogador1 = nomeJogador(1)
        jogador2 = nomeJogador(2)
        jogo = Nim(21, jogador1, jogador2)
    else:  
        jogador1 = nomeJogador(1)
        jogador2 = "Bot"
        jogo = Nim(21, jogador1, jogador2)

    jogo.jogar(modo)