valores = []
valores.append(5)
valores.append(3)
valores.append(4)
valores.sort()

for v in valores: #Percorre a lista e exibe
    print(f'{v}...')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(valores)