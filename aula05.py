''' Usando métodos publicos protegidos e privados'''

class Exemplo:
    def __init__(self):
        self.publico = "Eu sou publico"
        self._protegido = "Eu sou protegido"
        self.__privado = "Eu sou privado"

    def metodo_publico(self):
        return "Este metodo e publico"  

    def _metodo_protegido(self):
        return "Este metodo e protegido"

    def __metodo_privado(self):
        return "Este metodo e privado"  

# Usando a classe

obj = Exemplo()

print(obj.publico) #Acessa ao atributo público.
print(obj._protegido) # Acessa ao atributo protegido.
# print(obj.__privando) Isso resoltara em erro mais ainda e #possivel acessar de forma "indireta".
print(obj._Exemplo__privado) # Com name mangling aplicado.

# Usando o metodo

print(obj.metodo_publico())
print(obj._metodo_protegido())
# print(obj.__metodo_privado()) Isso tambem resultara em erro
print(obj._Exemplo__metodo_privado()) # Com o método mangling aplicado

