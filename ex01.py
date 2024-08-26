#Exercício 1: Números Primos
#Crie um programa que encontre e imprima os 20 primeiros números primos.
#Um número é considerado primo se ele é maior que 1 e possui exatamente
#dois divisores: 1 e ele mesmo. Utilize um loop while para iterar até
#encontrar 20 números primos e um loop for para contar a quantidade de
#divisores de cada número.'''


# Inicializa variáveis
primos_encontrados = 0  # Contador de números primos encontrados
num = 2  # Começa com o primeiro número inteiro maior que 1

# Loop para encontrar 20 números primos
while primos_encontrados < 20:
    # Conta os divisores do número atual
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    
    # Verifica se o número é primo (tem exatamente dois divisores: 1 e ele mesmo)
    if divisores == 2:
        print(num)  # Imprime o número primo
        primos_encontrados += 1  # Incrementa o contador de números primos
      
    # Incrementa o número para verificar o próximo
    num += 1
