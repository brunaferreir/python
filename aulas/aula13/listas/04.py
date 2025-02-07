a = [2,3,4,4,5]
b = a[:] # FATIAMENTO CRIA UMA COPIA DA LISTA podendo alterar o valor
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
