# Faça um programa que leia 5 vaores numericos e guarde-os em uma lista.
#No final, mostre qual foir o maior e o menor valor digitado e as suas respectivas posiçoes na lista

valores = []
for cont in range(1, 6):
    valores.append(int(input('Digite um valor ')))

print(valores)

maior_valor = max(valores)
indice_maior = valores.index(maior_valor)

menor_valor = min(valores)
indice_menor = valores.index(menor_valor)

print(f'O maior valor e: {maior_valor} e o indice do valor e {indice_maior}')
print(f'O menor valor e: {menor_valor} e o indice do valor e {indice_menor}')

