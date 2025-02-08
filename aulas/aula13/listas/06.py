#Crieum programa onde o usuario possa digitar varios valores numericos e 
# cadastra-os em uma lista.Caso o numero ja exista la dentro, ele não sera adicionado.No final, serão exibidos todos os valores unicos digitados em ordem crescentes

def adicionar(valores, elemento): 
    if elemento not in valores:
     valores.append(elemento)     

valores = []

r = 'S'
while r == 'S':
    try:
        elemento = int(input(f'Digite um numero '))
        adicionar(valores, elemento)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
   
    r = str(input('Quer continuar? [S/N] ')).upper()
 

print('FIM') 
valores.sort()  

print(valores)