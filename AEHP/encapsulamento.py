''' ENCAPSULAEMENTO PROTEGE SEU CODIGO
1 - TORNAR MUNDAÇAS INVISIVEIS
2 - FACILITAR A REUTILIZAÇÃO DE CODIGO
3 - REDUZIR EFEITOS COLATERAIS EFEITOS DANOSOS 
'''

class controleRemoto:
    def __init__(self, estado, volume):
        self.__set_ligdeslig(estado)
        self.__set_atualVolume(volume)

   #METODOS PRIVADOS

    def __get_ligdeslig(self): 
        return self.botao 

    def __set_ligdeslig(self, estado):
       self.botao = estado

    def __get_atualVolume(self): 
        return self.vol  

    def __set_atualVolume(self, volume):
        self.vol = volume
        
controle = controleRemoto("Estado: deligado", f'volume: {50}') #GET BUSCA
print(controle._controleRemoto__get_ligdeslig())
controle._controleRemoto__set_ligdeslig("Estado: ligado") #SET ALTERA 
print(controle._controleRemoto__get_ligdeslig())

print(controle._controleRemoto__get_atualVolume())


controle._controleRemoto__set_atualVolume(f'volume: {80}')
print(controle._controleRemoto__get_atualVolume())







        


