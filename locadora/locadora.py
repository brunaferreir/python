from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import date, timedelta   #permite trabalhar com datas e horarios.
from sqlalchemy import delete

#criando o motor do banco de dados criação e conexão do banco de dados com POO.
engine = create_engine('sqlite:///locadora.db')
Session = sessionmaker(bind=engine)  #Uma sessão é como uma transação, onde você pode executar várias operações antes de confirmar as mudanças no banco de dados.  
session = Session()

Base = declarative_base()   #Define uma classe base para todas as classes que representam tabelas no banco de dados.

class Diretor(Base):
    __tablename__ = 'diretores'   #Define o nome da tabela no banco de dados como "diretores".

    id = Column(Integer, primary_key=True) #Coluna de chave primária, um número inteiro único para cada diretor.
    nome = Column(String)
    nacionalidade = Column(String)

    def __repr__(self):
        return f'Diretor: {self.nome}\n filmes = {self.filmes})'

class Filme(Base):
    __tablename__ = 'filmes'
     
    id = Column(Integer, primary_key=True)
    titulo = Column(String) 
    anoLancamento = Column(Integer)  #indica que uma coluna em uma tabela de banco de dados armazenará valores numéricos inteiros.
    qtdDisponivel = Column(Integer)
    diretor_id = Column(Integer, ForeignKey('diretores.id'))   # é uma chave estrangeira.
    diretor = relationship('Diretor', backref='filmes')  #Define um relacionamento entre as classes Filme e Diretor. relationsh 
    #( 'Diretor', backref='filmes'): O primeiro argumento ('Diretor') especifica a classe relacionada, que é Diretor neste caso.
    #O argumento backref='filmes' cria uma referência inversa na classe Diretor. Isso significa que cada objeto Diretor terá uma #propriedade filmes que conterá uma lista de objetos Filme associados a ele.

    def __repr__(self):
        return f'Filme: (titulo={self.titulo}, diretor={self.diretor.nome})'


class Locacao(Base):
    __tablename__ = 'locação'
    
    id = Column(Integer, primary_key=True)
    nomeFilme = Column(String)
    data = Column(Date)
    disponibilidade = Column(Integer)
    cliente_cpf = Column(Integer, ForeignKey('clientes.cpf'))
    cliente = relationship('Cliente', backref='locação')
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'))
    funcionario = relationship ('Funcionario', backref='locação')
    
    
class Cliente(Base):
    __tablename__ = 'clientes'
    
    cpf = Column(Integer, primary_key=True)
    nome = Column(String)
    dataNasc = Column(String)
    sexo = Column(String)
    
class Funcionario(Base):
    __tablename__ = 'funcionarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    dataNasc = Column(String)
    sexo = Column(String)

class Multa(Base):
    __tablename__ = 'multas'

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    data = Column(Date)
    cliente_cpf = Column(Integer, ForeignKey('clientes.cpf'))
    cliente = relationship('Cliente', backref='multas')
    
# Criar todas as tabelas definidas  nas classes que herdam de BASE no banco de dados engine.
Base.metadata.create_all(engine)

def adicionar_diretor(nome, nacionalidade):   
    diretor = session.query(Diretor).filter_by(nome=nome).first()
    if not diretor:
        diretor = Diretor(nome=nome, nacionalidade = nacionalidade)
        session.add(diretor)
        session.commit()


def excluir_diretor(id_diretor):
    
    stmt = delete(Diretor).where(Diretor.id == id_diretor)

    session.execute(stmt)
    session.commit()

def adicionar_filme(titulo, anoLancamento, diretor, qtdDisponivel):
     diretor = session.query(Diretor).filter_by(nome=diretor).first()
     if not diretor:
         print(f"diretor: {diretor}, nao foi encontrado")
         return
    
     filme = Filme(titulo=titulo, anoLancamento=anoLancamento, diretor=diretor, qtdDisponivel=qtdDisponivel)
     session.add(filme)
     session.commit()

def cadastrar_cliente(nome, cpf, dataNasc, sexo):
    cliente = session.query(Cliente).filter_by(cpf=cpf).first()
    if cliente:
        print("Esse CPF já está cadastrado")
        return
    
    cliente = Cliente(nome=nome, cpf=cpf, dataNasc=dataNasc, sexo=sexo)
    session.add(cliente)
    session.commit()


def excluir_cliente(cpf):
    try:
        stmt = delete(Cliente).where(Cliente.cpf == cpf)

        session.execute(stmt, {'cpf': cpf})
        session.commit()

        print(f"Cliente com CPF {cpf} excluído com sucesso.")

    except Exception as e:
        print(f"Erro ao excluir cliente com CPF {cpf}: {str(e)}")



def fazer_locacao(nomeFilme, cpf):
    filme = session.query(Filme).filter_by(titulo=nomeFilme).first()
    if not filme or filme.qtdDisponivel <= 0:
        print("O filme está indisponível para locação no momento")
        return
    
    cliente = session.query(Cliente).filter_by(cpf=cpf).first()
    if not cliente:
        print("Cliente não encontrado.")
        return
    
    locacao = Locacao(nomeFilme=nomeFilme, cliente_cpf=cpf)
    locacao.data = date.today()
    filme.qtdDisponivel -= 1
    session.add(locacao)
    session.commit()
    print(f'Locação realizada! devolver em {locacao.data + timedelta(days=5)}')


def consultar_filmes():
    filmes = session.query(Filme).all()
    for filme in filmes:
        print(filme)

def consultar_diretores():
    diretores = session.query(Diretor).all()
    for diretor in diretores:
        print(diretor)

def consulta_locacoes():
    #faz acesso a tabela que queremos utilizar
    locacoes = session.query(Locacao).all()
    if not locacoes:
        print("Não há locações registradas.")
        return

    for locacao in locacoes:
        cliente_nome = locacao.cliente.nome
        print(f'Locação ID: {locacao.id}\n Nome do Filme: {locacao.nomeFilme}\n Data: {locacao.data}\n Cliente: {cliente_nome}')
        print('-'*20)

def devolucao(nomeFilme, cpf):
    pass

    
#adicionar diretor
#nome = input('Nome do Diretor: ') 
#nacionalidade = input('nacionalidade do diretor: ')
#adicionar_diretor(nome, nacionalidade)


# excluir diretor Solicitando o ID do diretor ao usuário
#id_diretor_str = input('id Diretor: ')
#print("excluido com sucesso")
#try:
#   id_diretor = int(id_diretor_str)
#   excluir_diretor(id_diretor)
#except ValueError:
#   print("ID do diretor inválido. Por favor, insira um número inteiro.")


#adicionar cliente
#nome= input('Nome do cliente que deseja adicionar: ')
#cpf = input('cpf: ')
#dataNasc = input('Data de Nascimento: ')
#sexo = input('sexo: ')
#cadastrar_cliente(nome, cpf, dataNasc, sexo)

# #excluir cliente
# cpf_usuario = input("Digite o CPF do cliente que deseja excluir: ")
# excluir_cliente(cpf_usuario)


# consultar_diretores()
# titulo = 'barbie'
# ano = 2010
# diretor = 'jk'
# qtdDisponivel = 3
# adicionar_filme(titulo, ano, diretor, qtdDisponivel)

# nomeFilme = 'barbie'
# nomeCliente = 'giovana'
# cpf = 12345678
# fazer_locacao(nomeFilme, nomeCliente, cpf)

#consulta_locacoes()

