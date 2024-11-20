# TRATAMENTO DE EXEÇÕES ERRO DE EXECUÇÃO

class DivisaoPorZeroError(Exception):
    """Exceção personalizada para divisão por zero."""
    pass

def dividir_numeros():
    try:
        # Solicita ao usuário para inserir dois números
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))

        # Verifica se o denominador é zero e lança uma exceção personalizada
        if denominador == 0:
            raise DivisaoPorZeroError("Erro: Você tentou dividir por zero.")

        # Tenta realizar a divisão
        resultado = numerador / denominador

    except ValueError:
        # Captura o erro caso o usuário não digite um número válido
        print("Erro: Por favor, insira um número válido.")
    
    except DivisaoPorZeroError as e:
        # Captura a exceção personalizada de divisão por zero
        print(e)

    except Exception as e:
        # Captura qualquer outro tipo de exceção que possa ocorrer
        print(f"Ocorreu um erro inesperado: {e}")
    
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
Erro: Você tentou dividir por zero.
Fim da operação.

Digite o numerador: dez
Erro: Por favor, insira um número válido.
Fim da operação.

Digite o numerador: 10
Digite o denominador: test
Erro: Por favor, insira um número válido.
Fim da operação.

exemplo_t ... _raise.py
Exibindo exemplo_try_except.py…
'''