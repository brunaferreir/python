class Pessoa:
    def __init__(self, nome, idade): # atributos
        self.nome = nome
        self.set_idade(idade)
    
    def set_idade(self, idade):
        while idade < 18:
            print("Idade invalida. A pessoa deve ser maior que 18!")
            idade = int(input("Insira uma idade valida: "))
            self.idade = idade
     
#classe filha
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):

         super().__init__(nome, idade)
         self.__salario = salario


    def get_salario(self):   #Obter o salario
        return self.__salario

    def set_salario(self, salario): #Atualizar salario
        self.__salario  = salario

    def calcular_salario_anual(self): 
       return self.__salario *12

 #Adicionou os objetos
funcionario1 = Funcionario("Bruna", 60, 2000)
funcionario2 = Funcionario("Renata", 28, 3200) 
funcionario3 = Funcionario("Manoel", 18, 3000) 


class Departamento:
    def __init__(self, nome_departamento):
        self.nome_departamento = nome_departamento
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def calcular_total_salarios(self):    #A função sum é uma função embutida neste caso, uma lista ou um gerador.
        total = sum(funcionario.calcular_salario_anual() 
        for funcionario in self.funcionarios)
        return total

    def listar_funcionarios(self):
        print(f"Funcionarios no departamento {self.nome_departamento}:")
        for funcionario in self.funcionarios:
            print(f"- {funcionario.nome}, Salario: R${funcionario.get_salario():.2f}, Salario Anual: R${funcionario.calcular_salario_anual():.2f}")


departamento = Departamento("RH")           

departamento.adicionar_funcionario(funcionario1)
departamento.adicionar_funcionario(funcionario2)
departamento.adicionar_funcionario(funcionario3)

funcionario1.set_salario(4500) 
print(f"Reajuste salarial da funcionaria {funcionario1.nome}: R${funcionario1._Funcionario__salario:.2f}" )

departamento.listar_funcionarios()

print("----------------------------------")

print(f"Total de salarios anuais do departamento: R${departamento.calcular_total_salarios():.2f}")
  

       


          



