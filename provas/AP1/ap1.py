import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def tirarPedra(self, valor):
        self.pedras = 21
        self.valor = valor
        while self.pedras != 1:
            if valor > 3 or valor <1:
                return print("O numero excede o valor limite")
            else:
                pedras -= self.valor
        print(f'jogador {self.jogador} perdeu')
        

    def vamosJogar(self, modo):  
        self.modo = modo
        print('Regras do Jogo')
        print('1- Numero total de pedras: 21')
        print('2- Limite máximo de retirada: 3')

        if modo == 1:
            while self.pedras != 1:
                valor = (int(input('digite o valor de pedras: ')))
                self.tirarPedra(valor)

        elif modo == 2:
            self.jogador = Jogador(str(input('insira o nome do jogador 1: ')))
        else:
            print("Modo invalido, digite novamente.")

    jogador1 = ("Lavina")
    vamosJogar(1)
