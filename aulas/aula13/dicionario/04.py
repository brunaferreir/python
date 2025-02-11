estado =dict() #criando dicionario
brasil = list()# crinado lista

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federal: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # faz copias da lista
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')