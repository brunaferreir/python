'''Exercício 7:

7. Agendamento de Eventos
Descrição: Implemente uma classe Evento com atributos para
nome do evento, data e número de participantes. Adicione
métodos para alterar a data do evento e outro para exibir as
informações do evento.'''

class evento:
    def __init__(self, nome, data, numero, participantes):
        self.nome = nome
        self.data = data
        self.numero = numero
        self.participantes = participantes

    def alterar_data(self, data):
        self.data = data

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Data: {self.data}')
        print(f'Numero: {self.numero}')
        print(f'Participantes: {self.participantes}')

e1 = evento('Bruna', '03/09/2024', '402', 30) 

e1.alterar_data('05/02/2025')

e1.info()        
