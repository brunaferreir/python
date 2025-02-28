'''Exercício 2: Jogo da Forca
Crie um programa que simule o jogo da forca. O computador escolhe uma palavra secreta de uma lista, e o jogador tenta adivinhar as letras da palavra. O jogador tem um número limitado de chances (ex: 6). O jogo termina quando o jogador acerta a palavra ou gasta todas as chances.
Exemplo de interação:

Adivinhe a palavra: _ _ _ _ _
Letra? a
_ a _ _ _
Letra? e
_ a _ _ e
...

Dicas:
Use listas para armazenar as palavras secretas e as letras adivinhadas.
Use loops while para controlar o fluxo do jogo.
Use condicionais if para verificar as entradas do jogador e dar feedback.
Use a função random.choice() para escolher uma palavra aleatória.
Observação:
Você pode usar o código do jogo de Craps como base para implementar esses exercícios. Adapte as funções e a lógica para as novas regras dos jogos.'''
 #Join Junte todos os itens de uma tupla em uma string

import random
palavras = ["casa", "carro", "computador", "python", "programacao", "jogo", "forca", "exercicio", "prova", "lista"]
palavra = random.choice(palavras)
palavra_secreta = ["_"] * len(palavra)
tentativas = 6
letras_erradas = []
while True:
    print("Palavra secreta:", " ".join(palavra_secreta))
    print("Letras erradas:", " ".join(letras_erradas))
    letra = input("Digite uma letra:")
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_secreta[i] = letra
    else:
        letras_erradas.append(letra)
        tentativas  -= 1
        if tentativas == 0:
            print("Voce perdeu! A palavra era:", palavra)
            break
    if "_" not in palavra_secreta:
        print("Voce acertou! A palavra era:", palavra)
        break
 