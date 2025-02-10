#Crie um progrma que vai ler varios numeros e colocar em uma lista.
#depois mostre:
# A)Quantos numeros foram digitados
#B)A lista ordenada de forma decrescente.
#C)Se o valor 5 foi digitado e esta ou nao na lista.

def adicionar(valores, elemento): 
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

if  5 not in valores:
      print("O valor 5 nao foi adicionado")  
else:
        print("O valor 5 foi adicionado")    


print(f'Essa lista tem {len(valores)} elementos')
valores.sort(reverse=True)
print(valores)