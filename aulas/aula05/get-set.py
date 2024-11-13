# Metodos GETTER e SETTER - Aula 05

class Pessoa:
    def __init__(self, idade_inicial):
        self.set_idade(idade_inicial)

    def get_idade(self):
        return self._idade    

    def set_idade(self, nova_idade):
       if nova_idade >= 0:
        self._idade = nova_idade   

# Usando a classe

pessoa = Pessoa(30)
print(pessoa.get_idade()) # Obtem a idade

pessoa.set_idade(35)
print(pessoa.get_idade()) # Atualiza a idade


# Tentativa de definir uma idade invalida 
pessoa.set_idade(-5)  # Não atualiza a idade 
print(pessoa.get_idade()) # A idade permanece a mesma

# Verificação da idade na criação do objeto
pessoa2 = Pessoa(-10)
print(dir(pessoa2))
print(pessoa2.get_idade())
# Cria o objeto, mas não o atributo _idade
