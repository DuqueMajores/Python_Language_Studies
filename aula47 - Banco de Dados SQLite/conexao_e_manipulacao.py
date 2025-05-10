import sqlite3
from sqlite3 import Error

#Aquivo de conexao com o banco de dados agenda.db

### Criando Conexao
def conexaoBanco():
    caminho = "C:/Users/Admin/Desktop/Cursos/Phyton/Python_Banco/agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho) 
    except Error as err:
        print(err)
    return con

### Criando Tabela
def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as err:
        print(err)

### Inserindo Dados
def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Inserido")
    except Error as err:
        print(err)

### Deletando Dados
def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Deletado")
    except Error as err:
        print(err)

### Atualizacao de registro na tabela
def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Atualizado")
    except Error as err:
        print(err)

### Consultando registro
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

