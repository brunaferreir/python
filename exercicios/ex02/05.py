'''5. Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números ímpares.'''

lista = []
pares = []
impares = []

for i in range(10):
    lista.append(int(input('Digite um número: ')))
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])    

print(lista) 
print(f"pares: {pares}")  
print(f"impares: {impares}") 