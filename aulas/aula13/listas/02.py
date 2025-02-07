#TUPLAS - SÃO CRIADAS  COM PARENTESES e sao imutaveis
#num = (2,3,3,5,3)

#Listas
num = [2,5,9,1]
num.append(4)
num.sort()
print(num)
num.sort(reverse= True)
num.insert(2, 0) #adicionou o 0 no indice 2
num.pop() #elimlina o ultimo valor da lista o 1
if 9 in num:
  num.remove(9)#elimina o primeiro valor da lista o 9
else:
  print("Nao achei o numero 9")  

print(num)
print(f'Essa lista tem {len(num)} elementos')

