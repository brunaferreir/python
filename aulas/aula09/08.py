'''Exercício 5: Sistema de Pagamento com Verificação
Implemente uma função `processar_pagamento(valor)` que recebe o valor de uma compra.
Se o valor for negativo ou zero, lance uma exceção personalizada `ValorInvalidoError`. Use
`try-except` para tratar o erro e solicite ao usuário que insira um valor válido até que o
processo seja concluído com sucesso.'''

class ValorInvalidoError(Exception):
    pass

def processar_pagamento(valor):
    try:
        valor = float(input("Digite o valor da compra: ")) 

        if valor <= 0:
            raise ValorInvalidoError(f"Valor negativo ou zero")
      
    
    except ValorInvalidoError as e:
        print(f"Erro {e}")

    else:
        print(f"Valor do pagamento: {valor}")
    
    finally:
        # Executa sempre, independentemente de exceção ocorrer ou não
        print("Fim da operação.") 
        return

processar_pagamento(0)
        


