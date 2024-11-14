#Abstração é o princípio de criar uma classe que contenha atributos e métodos que são comuns a outras classes e que podem servir como base para serem herdados.

#Você abstrai características comuns a N classes e fornece uma classe abstrata que pode ser herdada e servir de base para as demais.

# Permite que você se concentre nos aspectos importantes de uma aplicação, ignorando outros aspectos irrelevantes.

#decidir o que iremos representar e o que iremos ignorar.


from abc import ABC, abstractmethod

class Movel(ABC):
    def pintar(self) -> None:
        pass

class Cadeira(Movel):
    def __init__(self, n_pes) -> None:
        super().__init__()  
        self.n_pes = n_pes

    def montar(self) -> None:
        pass        

  