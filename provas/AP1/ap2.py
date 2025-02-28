import random

class Jogo:
    def __init__(self):
        self.pedras = 21
        self.jogador1 = None
        self.jogador2 = None

    def regras(self):
        print('Regras do Jogo')
        print('1- Numero total de pedras: 21')
        print('2- Limite máximo de retirada: 3')

    def jogar(self):
        self.regras()

        while True:
            modo = int(input('Digite o modo de jogo (1 para um jogador, 2 para dois jogadores): '))
            if modo == 1 or modo == 2:
                break
            else:
                print("Modo inválido, digite novamente.")

        if modo == 1:
            self.jogador1 = Jogador(input('Digite o nome do jogador: '))
            self.jogo_um_jogador()
        else:
            self.jogador1 = Jogador(input('Digite o nome do jogador 1: '))
            self.jogador2 = Jogador(input('Digite o nome do jogador 2: '))
            self.jogo_dois_jogadores()

    def jogo_um_jogador(self):
        while self.pedras > 1:
         
            self.pedras -= self.jogador1.tirar_pedra(int(input(f'{self.jogador1.nome}, digite o número de pedras para retirar (1-3): ')))
            if self.pedras <= 1:
                print(f'{self.jogador1.nome} perdeu!')
                break

           
            if self.pedras > 1:
                valor_computador = random.randint(1, min(3, self.pedras - 1))  
                self.pedras -= valor_computador
                print(f'Computador retirou {valor_computador} pedras.')
                if self.pedras <= 1:
                    print(f'{self.jogador1.nome} ganhou!')
                    break


    def jogo_dois_jogadores(self):
        while self.pedras > 1:
            self.pedras -= self.jogador1.tirar_pedra(int(input(f'{self.jogador1.nome}, digite o número de pedras para retirar (1-3): ')))
            if self.pedras <= 1:
                print(f'{self.jogador1.nome} perdeu!')
                break

            self.pedras -= self.jogador2.tirar_pedra(int(input(f'{self.jogador2.nome}, digite o número de pedras para retirar (1-3): ')))
            if self.pedras <= 1:
                print(f'{self.jogador2.nome} perdeu!')
                break

class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def tirar_pedra(self, valor):
        if valor > 3 or valor < 1:
            print("O número excede o valor limite")
            return 0
        else:
            return valor

jogo = Jogo()
jogo.jogar()