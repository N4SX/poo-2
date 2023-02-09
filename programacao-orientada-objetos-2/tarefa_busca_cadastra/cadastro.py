import mysql.connector as mysql
from pessoa import Pessoa

class Cadastro():
    
    def __init__(self):
        self.conexao = mysql.connect( host = 'localhost', db = 'poo2', user = 'root', passwd = '24121998')
        self.cursor = self.conexao.cursor()
        self.sql = """CREATE TABLE IF NOT EXISTS usuarios(nome varchar(30) NOT NULL, endereco varchar(50) NOT NULL , cpf varchar(15) PRIMARY KEY, nascimento varchar(15) NOT NULL);"""  
        self.cursor.execute(self.sql)
        self.conexao.commit()
        
    def cadastra(self, pessoa):

        existe = self.busca(pessoa.cpf)

        if (existe==None):
            self.cursor.execute('INSERT INTO usuarios(nome,cpf,endereco,nascimento) VALUES(%s,%s,%s,%s)',(pessoa.nome,pessoa.cpf,pessoa.endereco,pessoa.nascimento))
            self.conexao.commit()
            return True 
        else:
            return False
            
    def busca(self, cpf):
        
        self.cursor.execute('SELECT * FROM usuarios WHERE cpf = %s', (cpf,))
        rt = self.cursor.fetchone()

        if rt == None:
            return None
        else:
            pessoa = Pessoa(rt[0],rt[1],rt[2],rt[3])
            return pessoa