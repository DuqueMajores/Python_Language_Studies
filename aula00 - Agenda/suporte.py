import sqlite3
from sqlite3 import Error

local = "C:/Users/Admin/Desktop/Cursos/Phyton/Python_Banco/"
banco = "agenda.db"

### Conexao
def conexao():
    caminho = f"{local}{banco}"
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

### Inserindo dados
def cadastrar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados Cadastrados")
    except Error as err:
        print(err)

### Consultar Registro
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

### Alterar Dados do Registro
def alterar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Alterado")
    except Error as err:
        print(err)

### Deletar Registro
def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Deletado")
    except Error as err:
        print(err)

