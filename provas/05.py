'''Exercício 4: Jogo de Bingo
Crie um programa que simule um jogo de bingo simplificado. O programa gera um cartão de bingo aleatório para o jogador (com números entre 1 e 75) e, em seguida, sorteia números aleatórios. O jogador marca os números em seu cartão e o jogo continua até que o jogador complete uma linha, coluna ou diagonal (ou seja, faça um "bingo").

Exemplo de interação:

Seu cartão de bingo:
[12, 34, 56, 70, 23]
[45, 67, 8, 9, 51]
...

Número sorteado: 34
Você marcou o número 34!

...

Bingo! Você ganhou!
Dicas:
Use a função random.choice() para a escolha aleatória do computador.
Use loops while para controlar as rodadas do jogo.
Use condicionais if para determinar o vencedor em cada rodada e para verificar se o jogador fez um bingo.
Observação:'''

import random
cartao = []
for i in range(3):
    linha = random.sample(range(1, 76), 3)
    cartao.append(linha)
print("Seu cartao de bimgo:")
for linha in cartao:
    print(linha) 
while True:
    num_sorteado = random.randint(1, 75)
    print("Numero sorteado:", num_sorteado)
    for linha in cartao:
        for i in range(3):
            if linha[i] == num_sorteado:
                linha[i] = "X"
    print("Seu cartao de bingo:")
    for linha in cartao:
        print(linha)
    linha1 = cartao[0]
    linha2 = cartao[1]
    linha3 = cartao[2]
    if linha1 == ["X", "X", "X"] or linha2 == ["X", "X", "X"] or linha3 == ["X", "X", "X"]:
        print("Bingo! Voce ganhou!")
        break

            

