''' Exercício 1: Sistema de Biblioteca
Desenvolva um sistema básico para gerenciar o acervo de uma biblioteca.
**Tarefas:**
1. Crie uma classe `Livro` com os atributos: título, autor, ISBN e status (disponível ou emprestado).
2. Implemente métodos para:
   - Emprestar um livro (se estiver disponível).
   - Devolver um livro.
   - Exibir o catálogo completo do livro.'''


class Livro:
   def __init__(self, titulo, autor, isbn):
      self.titulo = titulo
      self.autor = autor
      self.isbn =  isbn
      self.status = 'disponivel' 

   def emprestar_livro(self):
      if self.status == 'disponivel': 
         self.status = 'indisponivel'
         print(f'O livro {self.titulo} foi emprestado')    
      else:
         print(f'O livro {self.titulo} ja foi emprestado')

   def devolver_livro(self):
      if self.status == 'indisponivel':
         self.status = 'disponivel'
         print(f'O livro {self.titulo} foi devolvido')
      else:
         print(f'O livro {self.titulo} ja esta disponivel.')   
         
   def exibir_catalogo(self):
         print(f'tutulo: {self.titulo}')
         print(f'Autor: {self.autor}')
         print(f'ISBN: {self.isbn}')
         print(f'Status: {self.status}')


l1 = Livro('Sapiens', 'sapo', 2232232)

l1.exibir_catalogo()

l1.emprestar_livro()

l1.devolver_livro()

l1.exibir_catalogo()

























   