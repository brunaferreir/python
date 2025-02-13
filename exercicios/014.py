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