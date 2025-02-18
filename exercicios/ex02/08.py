'''8. Jogo de Craps: Crie um programa que simule um jogo de Craps. O jogo
funciona da seguinte maneira:
O jogador lança dois dados, resultando em um valor entre 2 e 12.
Na primeira jogada:
 Se o resultado for 7 ou 11, o jogador vence automaticamente (chamado
de &quot;natural&quot;).
 Se o resultado for 2, 3 ou 12, o jogador perde imediatamente (chamado
de &quot;craps&quot;).
 Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o &quot;Ponto&quot; do
jogador.
Caso um &quot;Ponto&quot; tenha sido estabelecido, o jogador continua lançando os
dados:
 Se tirar o mesmo valor do Ponto, ele vence.
 Se tirar um 7 antes de repetir o Ponto, ele perde.
Implemente a lógica para simular esse jogo e exiba o resultado de cada jogada.'''



import random

def lancar_dados():
    """Simula o lançamento de dois dados de 6 faces e retorna a soma dos resultados."""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jogar_craps():
    """Simula um jogo de Craps."""
    ponto = 0
    primeira_jogada = True

    while True:
        resultado = lancar_dados()
        print(f"Resultado dos dados: {resultado}")

        if primeira_jogada:
            if resultado == 7 or resultado == 11:
                print("Voce venceu! Natural!")
                return "vitoria"
            elif resultado == 2 or resultado == 3 or resultado == 12:
                print("Voce perdeu! Craps!")
                return "derrota"
            else:
                ponto = resultado
                print(f"Seu ponto: {ponto}")
                primeira_jogada = False
        else:
            if resultado == ponto:
                print("Voce venceu! Você atingiu seu ponto!")
                return "vitoria"
            elif resultado == 7:
                print("Voce perdeu! Saiu um 7 antes do seu ponto!")
                return "derrota"


resultado_jogo = jogar_craps()
print(f"Resultado final do jogo: {resultado_jogo}")