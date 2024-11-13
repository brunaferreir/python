'''Exercício 5:

5. Registro de Alunos
Descrição: Crie uma classe Aluno com atributos para nome,
matrícula e curso. Adicione métodos para mudar o curso do
aluno e outro para exibir as informações do aluno.'''

class aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mudar_curso(self, curso):
        self.curso = curso

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Matricula: {self.matricula}')
        print(f'Curso: {self.curso}')

a1 = aluno('Bruna', '2401556', 'ADS') 

a1.mudar_curso('si')

a1.info()



