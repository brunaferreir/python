# TRATAMENTO DE EXEÇÕES ERRO DE EXECUÇÃO
def dividir_numeros():
    try:
        # Solicita ao usuário para inserir dois números
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))

        # Tenta realizar a divisão
        resultado = numerador / denominador

    except ValueError:
        # Captura o erro caso o usuário não digite um número
        print("Erro: Por favor, insira um número válido.")
    
    except ZeroDivisionError:
        # Captura o erro caso o denominador seja zero
        print("Erro: Não é possível dividir por zero.")
    
    else:
        # Se não ocorrer nenhuma exceção, exibe o resultado
        print(f"O resultado da divisão é: {resultado}")
    
    finally:
        # Executa sempre, independentemente de exceção ocorrer ou não
        print("Fim da operação.")

# Executa a função
dividir_numeros()

#Casos de Teste
'''
Digite o numerador: 10
Digite o denominador: 2
O resultado da divisão é: 5.0
Fim da operação.

Digite o numerador: 10
Digite o denominador: 0
Erro: Não é possível dividir por zero.
Fim da operação.

Digite o numerador: dez
Erro: Por favor, insira um número válido.
Fim da operação.

exemplo_ ... xcept.py
Exibindo exemplo_try_except.py…
'''