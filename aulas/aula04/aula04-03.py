'''Exercício 3:

3. Sistema de Biblioteca
Descrição: Desenvolva uma classe Livro com atributos para título,
autor, ano de publicação e disponibilidade. Adicione métodos
para emprestar e devolver o livro, alterando seu status de
disponibilidade.'''

class livro:
     def __init__(self, titulo, autor, ano, dispo):
          self.titulo = titulo
          self.autor = autor
          self.ano = ano
          self.dispo = dispo 

     def emprestar(self, dispo):
        if self.dispo >= dispo:
            self.dispo -= dispo
            print("Livro emprestado")
        else:
            print("Não está disponivel")
     def devolver(self, dispo):
            self.dispo += dispo

     def info(self):
        print(f'titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano: {self.ano}')
        
               

v1 = livro('Vida', 'Jose', 2024, 5) 

v1.emprestar(2)

v1.info()
            
            

