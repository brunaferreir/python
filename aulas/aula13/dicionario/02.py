pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f' O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.items())

for k in pessoas.keys():
    print()

del pessoas['sexo']  #deletar um elemento
pessoas['peso'] = 98.5 #adicionar um elemento

for k, v in pessoas.items():
    print (f'{k} = {v}') 

