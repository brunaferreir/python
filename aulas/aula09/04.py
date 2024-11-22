'''Exercício 1: Validação de Entrada Numérica
Crie uma função `ler_numero( )` que solicita ao usuário que insira um número inteiro. Se o
usuário inserir algo que não seja um número inteiro, a função deve levantar uma exceção
personalizada `EntradaInvalidaError` e tratar a exceção para exibir uma mensagem

amigável. Dica: Para verificar se uma string é composta por dígitos numéricos, utilize o
método `isdigit( )`, que retorna True se a string é composta por números.'''

class EntradaInvalidaError(Exception):
    """Exceção personalizada para entradas inválidas."""
    pass

def ler_numero():
    """Solicita ao usuário um número inteiro e valida a entrada."""
    try:
        entrada = input("Insira um número inteiro: ")

        if not entrada.isdigit():
            raise EntradaInvalidaError("A entrada fornecida não é um número inteiro.")
        return int(entrada)
    except EntradaInvalidaError as e:
        print(f"Erro: {e}")
        return ler_numero()  # Solicitar novamente

# Exemplo de uso
numero = ler_numero()
print(f"Você inseriu o número: {numero}")








    