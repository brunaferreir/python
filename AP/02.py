'''Exercício 2: Sistema de Gerenciamento de Funcionários
Implemente um sistema para gerenciar as informações de funcionários em uma empresa.

**Tarefas:**
1. Crie uma classe `Funcionario` com os atributos: nome, cargo, salário e número de identificação.
2. Implemente métodos para:
   - Aumentar o salário de um funcionário.
   - Exibir as informações completas de um funcionário.
   - Promover um funcionário (alterar o cargo e ajustar o salário).
   
**Desafio Extra:**  
- Crie uma classe `Departamento` que contenha uma lista de funcionários e métodos para exibir todos os funcionários de um departamento e calcular o custo total de salários.'''

class Funcionario:
   def __init__(self, nome, cargo, salario, codigoID):
      self.nome = nome
      self.cargo = cargo
      self.salario = salario
      self.codigoID = codigoID

   def aumentar_salario(self, salario): 
     self.salario  += salario

   def info(self):
      print(f'Nome: {self.nome}')
      print(f'Cargo: {self.cargo}')
      print(f'Salario: {self.salario}')
      print(f'CodigoID: {self.codigoID}')
      print()

   def promover_funcionario(self, salario, cargo):
      self.cargo = cargo
      self.salario = salario

class Departamento:
   def __init__(self, nome_departamento):
      self.nome_departamento  = nome_departamento
      self.funcionarios = []
   
   def adicionar_funcionario(self, funcionario):
      self.funcionarios.append(funcionario)

   def exibir_funcionarios(self):
      for funcionario in self.funcionarios:
         funcionario.info()
  

f1 = Funcionario('Bruna', 'Desenvolvedor(a)', 4000, 32456)
f2 = Funcionario('Lirio', 'Analista', 5400, 34567)
f3 = Funcionario('Bernardo', 'Scrum master', 9000, 45676)

dep1 = Departamento('T.I')

dep1.adicionar_funcionario(f1)
dep1.adicionar_funcionario(f2)
dep1.adicionar_funcionario(f3)

f1.aumentar_salario(1000)

print()

f1.promover_funcionario('designer', 6000)

dep1.exibir_funcionarios()













