'''Exercício 6: Sistema de Agendamento de Consultas Médicas
Implemente um sistema básico de agendamento de consultas para uma clínica.

**Tarefas:**
1. Crie uma classe `Consulta` com os atributos: nome do paciente, nome do médico, data e status (agendada, realizada, cancelada).
2. Implemente métodos para:
   - Agendar uma consulta.
   - Cancelar uma consulta.
   - Exibir todas as consultas agendadas.

**Desafio Extra:**  
- Adicione um método para verificar a disponibilidade do médico antes de agendar a consulta.
- Implemente uma função que exibe o histórico de consultas de um determinado paciente.

Esses exercícios te ajudarão a praticar a criação de classes, gerenciamento de atributos e métodos, além de desenvolver a lógica de sistemas complexos.'''




class Consulta:
    def __init__(self, nome_paciente, nome_medico, data, status="agendada"):
        self.nome_paciente = nome_paciente
        self.nome_medico = nome_medico
        self.data = data
        self.status = status

    def agendar(self):
        if self.status != "agendada":
            raise ValueError("Consulta já está agendada ou cancelada.")
        print(f"Consulta agendada para {self.nome_paciente} com Dr(a). {self.nome_medico} em {self.data}.")

    def cancelar(self):
        if self.status == "cancelada":
            raise ValueError("Consulta já está cancelada.")
        self.status = "cancelada"
        print(f"Consulta de {self.nome_paciente} cancelada.")

    def __str__(self):
        return f"Paciente: {self.nome_paciente}, Medico: {self.nome_medico}, Data: {self.data}, Status: {self.status}"

# Exemplo de uso:
consulta1 = Consulta("Joao Silva", "Maria Almeida", "2023-11-25")
consulta1.agendar()

consulta2 = Consulta("Ana Souza", "Pedro Santos", "2023-11-26")
consulta2.cancelar()  # Gera um erro, pois a consulta ainda não foi agendada

# Para exibir todas as consultas (em um cenário mais real, você teria uma lista de consultas)
consultas = [consulta1]
for consulta in consultas:
    print(consulta)