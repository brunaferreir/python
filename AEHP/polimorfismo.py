#para ter Polimorfismo precisa ter hereança.

# FUNDAMENTO 
# Diversas metodos (CALCULAR_SALARIO) com o mesmo nome 
# executando funções diferentes.

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
      pass 

class Analista(Funcionario):
   def calcular_salario(self):
      return self.salario_base + 0.1 * self.salario_base #bonus de 10%
   
class Gerente(Funcionario):
   def __init__(self, nome, salario_base, bonus):
      super().__init__(nome, salario_base)  
      self.bonus  = bonus

   def calcular_salario(self):
      return self.salario_base + self.bonus   
   
class Estagiario(Funcionario):
   def calcular_salario(self):
      return self.salario_base #estagiario não recebe bônus 
   

def exibir_salario(funcionario):
   return funcionario.calcular_salario()




analista = Analista(nome="Ana", salario_base=5000)
gerente = Gerente(nome="Carlos", salario_base=8000, bonus=2000)
estagiario = Estagiario(nome="Eduardo", salario_base=2000)


print(f"Salario de {analista.nome}: R${exibir_salario(analista):,.2f}")
print(f"Salario de {gerente.nome}: R${exibir_salario(gerente):,.2f}")
print(f"Salario de {estagiario.nome}: R${exibir_salario(estagiario):,.2f}")
 
