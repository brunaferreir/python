'''Exercício 1: Jogo de Adivinhação
Cr/ie um programa que simule um jogo de adivinhação. O computador gera um número aleatório entre 1 e 100, e o jogador tenta adivinhar o número. O programa dá dicas como "muito alto" ou "muito baixo" até que o jogador acerte.
Exemplo de interação:
Tente adivinhar o número entre 1 e 100: 50
Muito baixo!
Tente adivinhar o número entre 1 e 100: 75
Muito alto!
Tente adivinhar o número entre 1 e 100: 62
Parabéns! Você acertou em 3 tentativas.'''

import random

num = random.randint(1,100)
tentativas = 0
while True:
    tentativa = int(input("Tente adivinhar o numero de 1 a 100:"))
    tentativas += 1
    if tentativa == num:
        print("Parabens! Voce acertou!")
        print(f"Voce acertou em {tentativas} tentativas")
        break
    elif tentativa < num:
        print("Muito baixo!")
    elif tentativa > num:
        print("Muito alto!")
       


