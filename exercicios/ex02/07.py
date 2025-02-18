'''7. Numa eleição existem três candidatos. Faça um programa que peça o
número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
número de votos de cada candidato.'''

eleitores = 10
votos = []
c1 = []
c2 = []
c3 = []

for  i in range(eleitores):
    votos.append(int(input("Digite o numero do canditato que deseja votar:")))
    if votos[i] == 13:
        c1.append(votos[i])
    elif votos[i] == 22:
        c2.append(votos[i])
    elif votos[i] == 50:     
        c3.append(votos[i])

print(f"Votos candidato 13: {len(c1)}")
print(f"Votos candidato 22: {len(c2)}")
print(f"Votos candidato 50: {len(c3)}")        
