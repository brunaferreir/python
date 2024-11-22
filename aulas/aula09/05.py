'''Exercício 2: Função de Raiz Quadrada com Tratamento de Exceções
Crie uma função `calcular_raiz_quadrada(numero)` que recebe um número como argumento
e retorna a raiz quadrada desse número. Se o número for negativo, a função deve lançar
uma exceção personalizada `NumeroNegativoError` e capturar essa exceção para exibir
uma mensagem de erro. Dica: Você pode usar o módulo math para calcular a raiz quadrada
usando o método `math.sqrt(numero) 
`'''
import math

class NumeroNegativoError(Exception):
    """Exceção personalizada para numero negativo."""
    pass

def calcular_raiz_quadrada(numero):
    try:
        numero = int(input("Digite um numero: "))

        if numero < 0 :
            raise NumeroNegativoError("A entrada deve ser um numero positivo")
        
        resultado = math.sqrt(numero) 

    except NumeroNegativoError as e:
        print(f"Erro: {e}")
      
    else:
        print(f"A raiz quadrada do numero é: {resultado}")
    
    finally:
        # Executa sempre, independentemente de exceção ocorrer ou não
        print("Fim da operação.")
 
calcular_raiz_quadrada(0)

    
  
