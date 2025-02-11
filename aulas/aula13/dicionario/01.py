#Um dicionário em Python é uma estrutura de dados que permite armazenar dados em pares. Chamamos cada par de dados de par chave-valor. Assim, cada elemento em um dicionário consiste em uma chave e um valor associado a essa chave. Podemos utilizar esta associação para representar relações que existem no mundo real, como um produto e seu preço.

#Adicionar dados em um DICIONARIO o append nao fulciona
#dados['sexo'] = 'M'
filme = {'titulo': 'star wars',
         'ano': 1977,
         'diretor': 'Gorge lucas'}

print(filme.values()) #retorna apenas os valores
print(filme.keys()) #retorna apenas as chaves
print(filme.items()) #retorna tanto as chaves quanto os valores 

for k, v in filme.items():
    print(f'O {k} e {v}')



