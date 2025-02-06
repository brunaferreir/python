lanches = ['dog','aburguer','suco', 'pizza', 'picole', 'cookies']
print(lanches)

if 'pizza' in lanches:
    lanches.remove('pizza')
print(lanches)


valores = list(range(1,11))
print(valores)

#ORDENAR VALORES SORT
valores2 = [2,4,6,2,8,6,0]
valores2.sort()
print(valores2)

#ORDENAR VALORES NA ORDE DECRESCENTE SORT REVERSE
valores3 = [2,4,6,2,8,6,0]
valores3.sort()
valores3.sort(reverse= True)
print(valores3)

#QUANTOS ELEMENTOS EXISTEM NA LISTA
print(len(valores))

