'''Exercício 4: Cálculo de Média com Validação
Escreva uma função `calcular_media(notas)` que recebe uma lista de notas e calcula a
média. Se a lista contiver um valor que não seja um número (exemplo: uma string), a função
deve lançar uma exceção personalizada `NotaInvalidaError`. O bloco `try-except` deve
capturar e tratar essa exceção. Dica: Você pode verificar se a nota é int ou float com a função
`isinstance(nota, (int, float)) `.'''


# Definindo a exceção personalizada
class NotaInvalidaError(Exception):
    def __init__(self, mensagem="A lista contém uma ou mais notas inválidas!"):
        super().__init__(mensagem)

# Função para calcular a média
def calcular_media(notas):
    
    try:
        # Verifica se todas as notas são válidas
        for nota in notas:
            if not isinstance(nota, (int, float)):
                raise NotaInvalidaError(f"Nota invalida encontrada: {nota}")
        
        # Calcula a média se todas as notas forem válidas
        media = sum(notas) / len(notas)
        return media
    
    except NotaInvalidaError as e:
        print(f"Erro: {e}")
        return None

# Exemplo de uso
try:
  
    notas = [9, 9, 9]
  
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")

print("Media com notas validas:", calcular_media(notas))
