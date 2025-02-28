'''Exercício 3: Jogo de Pedra, Papel e Tesoura
Crie um programa que simule o jogo de Pedra, Papel e Tesoura entre o jogador e o computador. O jogador escolhe sua opção (pedra, papel ou tesoura) e o computador também escolhe aleatoriamente. O programa então determina o vencedor ou se houve empate.

Exemplo de interação:

Escolha sua opção: pedra, papel ou tesoura: papel
O computador escolheu: tesoura
Você perdeu!'''
import random
opcoes = ["pedra", "papel", "tesoura"]
for i  in range(5):
    jogador = input("Escolha sua opcao: pedra, papel ou tesoura:")
    comp = random.choice(opcoes)
    print(f"O computador escolheu: {comp}")
    if jogador == "pedra" and comp  == "tesoura":
        print("Voce venceu!")
    elif jogador == "papel" and comp =="pedra":
        print("Voce venceu!")   
    elif jogador == "tesoura" and comp == "papel":
        print("Voce venceu!") 
    elif jogador == comp:
        print("Empate!")
    else:
        print("Voce perdeu!")            