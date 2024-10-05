class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.cargo = cargo
        self.set_idade(idade)
    
    def set_idade(self, idade):
        while idade < 18:
            idade = int(input('Idade inválida, insira nova idade: '))
        self.idade = idade

class membroEquipe(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade, cargo)
        self.__horas_trabalhadas = 0
    
    def get_horas_trabalhadas(self):
        return self.__horas_trabalhadas

    def adicionar_horas(self, horas):
        if horas > 0:
            self.__horas_trabalhadas += horas
        else:
            print('Hora deve ser maior que zero.')
    
    def mostrar_detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.cargo}')

class Projeto:
    def __init__(self, nome_projeto):
        self.nome_projeto = nome_projeto
        self.membros = []
    
    def adicionar_membro(self, membro):
        self.membros.append(membro)
    
    def calcular_total_horas(self):
        total = 0
# PERCORRE A LISTA SOMANDO TODAS AS HORAS TRABALHADAS
        for membro in self.membros: 
            total += membro.get_horas_trabalhadas()
        return total
    
    def listar_membros(self):
        for membro in self.membros:
            membro.mostrar_detalhes()
            print(f'Horas trabalhadas: {membro.get_horas_trabalhadas()}')
    
    def remover_membro(self, nome):
        for membro in self.membros:
            if membro.nome == nome:
                self.membros.remove(membro)
                print('Membro removido')
    
m1 = membroEquipe('João', 58, 'Diretor')
m2 = membroEquipe('Maria', 47, 'Diretora')
m3 = membroEquipe('José', 80, 'Estagiário')

proj1 = Projeto('Projeto_Piloto')

proj1.adicionar_membro(m1)
proj1.adicionar_membro(m2)
proj1.adicionar_membro(m3)

m1.adicionar_horas(20)
m2.adicionar_horas(40)
m3.adicionar_horas(60)

proj1.listar_membros()

print(f'Total de horas trabalhadas: {proj1.calcular_total_horas()}')

proj1.remover_membro('José')

proj1.listar_membros()
