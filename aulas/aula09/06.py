'''Exercício 3: Sistema de Cadastro de Idade
Crie uma função `cadastrar_idade()` que solicita a idade de um usuário. Se o usuário inserir
um valor negativo ou maior que 120, uma exceção personalizada `IdadeInvalidaError` deve
ser levantada e tratada. O sistema deve continuar solicitando uma idade válida até que o
usuário forneça uma entrada correta.'''

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade():
    try:
        idade = int(input("Digite sua idade: "))

        while idade < 0 or idade > 100:
            raise IdadeInvalidaError(f"Idade invalida") 
        return int(idade)                   
    except IdadeInvalidaError as e:
         print(f"Erro: {e}")
         return cadastrar_idade()

Idade = cadastrar_idade()
print(f"Você inseriu o número: {Idade}")


        

