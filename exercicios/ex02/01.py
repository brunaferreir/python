'''Jogo de Craps: Crie um programa que simule um jogo de Craps. O jogo
funciona da seguinte maneira: O jogador lança dois dados, resultando em um valor entre 2 e 12.
Na primeira jogada: Se o resultado for 7 ou 11, o jogador vence automaticamente (chamado de "natural").
 Se o resultado for 2, 3 ou 12, o jogador perde imediatamente (chamado
de craps).
Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o Ponto do
jogador.
Caso um Ponto tenha sido estabelecido, o jogador continua lançando os
dados:
 Se tirar o mesmo valor do Ponto, ele vence.
Se tirar um 7 antes de repetir o Ponto, ele perde.
Implemente a lógica para simular esse jogo e exiba o resultado de cada jogada.'''

"""
    Simula o lançamento de dois dados de 10 faces e retorna os resultados.

    Args:
        dado1: Variável que irá armazenar o resultado do primeiro dado.
        dado2: Variável que irá armazenar o resultado do segundo dado.

    Returns:
        Uma tupla contendo os resultados dos dois dados.
    """


import random

def lancar_dados(dado1, dado2):
    dado1 = random.randint(2, 12)
    dado2 = random.randint(2, 12)
    return dado1, dado2
# Exemplo de uso da função
resultado_dado1, resultado_dado2 = lancar_dados(0, 0)  # Inicializa as variáveis com 0

if resultado_dado1  == 7 or resultado_dado1 == 11:
    print("Natural! Voce venceu!")
elif resultado_dado1  == 2 or resultado_dado1 == 3 or resultado_dado1 == 12:
    print("Craps! Voce perdeu!")
elif resultado_dado1 or resultado_dado2 == 4 or resultado_dado1 or resultado_dado2 == 5 or resultado_dado1 or resultado_dado2 == 6 or resultado_dado1 or resultado_dado2 == 8 or resultado_dado1 or resultado_dado2 == 9 or resultado_dado1 or resultado_dado2 == 10:
    ponto = resultado_dado1
    print("Ponto! Continue jogando!")    
    print(f"Seu ponto e: {ponto}")
    if  resultado_dado1 or resultado_dado2 == ponto:
        print("Voce venceu!")


print(f"Resultado do primeiro dado: {resultado_dado1}")
print(f"Resultado do segundo dado: {resultado_dado2}")

