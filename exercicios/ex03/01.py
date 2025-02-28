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

#jogador = input(str("Digite o nome do jogador:"))
dado1 = random.randint(1,6)
dado2 =random.randint(1,6)
resultado = dado1 + dado2
print(f"Dado1 = {dado1} dado2 = {dado2} resultado = {resultado}")
if resultado == 7 or resultado == 11:
    print(f"O jogador(a)  venceu!")
elif resultado == 2 or resultado == 3 or resultado == 12:
    print(f"O jogador(a) perdeu!")    
else: 
    print(f"O jogador(a) continua jogando")   
    while True:
        dado3 = random.randint(1,6) 
        dado4 = random.randint(1,6)
        resultado2 = dado3 + dado4
        print(f"Dado1 = {dado3} dado2 = {dado4} resultado = {resultado2}")
        if resultado2 == resultado:
            print(f"O jogador(a) venceu!")
            break
        if resultado2 == 7:
            print(f"O jogador(a)perdeu!")
            break
