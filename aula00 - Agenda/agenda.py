import suporte
import os

opc = 0
loop = True

vcon = suporte.conexao()
"""tabela = "CREATE TABLE tb_agenda(
                N_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                T_NOME VARCHAR(30),
                T_TELEFONE VARCHAR(14),
                T_EMAIL VARCHAR(30));"""
#suporte.criarTabela(vcon, tabela)

def dot():
    print("------------------------------------")
def cadastro():
    try:
        nome = str(input("Nome....: "))
        tel = str(input("Telefone: "))
        em = str(input("E-mail..: "))
    except ValueError as err:
        print(err)

    vsql = f"INSERT INTO tb_agenda(T_NOME, T_TELEFONE, T_EMAIL) VALUES('{nome}', '{tel}', '{em}')"
    suporte.cadastrar(vcon, vsql)

    dot()
    opc = str(input("Continuar? [s/n]: "))
    dot()

    if opc == "s" or opc == "S":
        cadastro()
    else:
        pass
def consulta():
    opconsul = int(input("Procurar por:\n1.ID\n2.Nome\n3.Telefone\n4.Email\n5.Todos\nOpcao: "))

    if opconsul == 1:
        dot()
        idnum = str(input("Numero do ID: "))
        vsql = f"SELECT * FROM tb_agenda WHERE N_ID LIKE '{idnum}' "
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(str(dados[1] + "\n" + dados[2] + "\n" + dados[3]))
            dot()
    elif opconsul == 2:
        dot()
        tnome = str(input("Cunsultar nome: "))
        vsql = f"SELECT * FROM tb_agenda WHERE T_NOME LIKE '{tnome}%'"
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
    elif opconsul == 3:
        dot()
        ttel = str(input("Consultar telefone: "))
        vsql = f"SELECT * FROM tb_agenda WHERE T_TELEFONE LIKE '{ttel}%'"
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
    elif opconsul == 4:
        dot()
        tem = str(input("Consultar Email: "))
        vsql = f"SELECT * FROM tb_agenda WHERE T_EMAIL LIKE '{tem}%'"
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
    elif opconsul == 5:
        dot()
        vsql = "SELECT * FROM tb_agenda"
        res = suporte.consultar(vcon, vsql)
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
    else:
        dot()
        print("Opcao Invalida")
def altera():
    opalter = int(input("Pesquisar por:\n1.ID\n2.Nome\n3.Telefone\n4.E-mail\nOpcao: "))

    if opalter == 1:
        dot()
        nid = str(input("Numero do ID: "))
        vsql = f"SELECT * FROM tb_agenda WHERE N_ID LIKE '{nid}'"
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
        
        dadoalter = int(input("Alterar:\n1.Nome\n2.Telefone\n3.E-mail\nOpcao: "))

        if dadoalter == 1:
            dot()
            name = str(input("Nome: "))
            newname = str(input("Novo Nome: "))
            namesql = f"UPDATE tb_agenda SET T_NOME='{newname}' WHERE T_NOME LIKE '{name}'"
            suporte.alterar(vcon, namesql)
        if dadoalter == 2:
            dot()
            newtel = str(input("Novo Telefone: "))
            telsql = f"UPDATE tb_agenda SET T_TELEFONE='{newtel}' WHERE N_ID LIKE '{nid}'"
            suporte.alterar(vcon, telsql)
        if dadoalter == 3:
            dot()
            em = str(input("E-mail: "))
            newem = str(input("Novo E-mail: "))
            emsql = f"UPDATE tb_agenda SET T_EMAIL='{newem}' WHERE T_EMAIL LIKE '{em}'"
            suporte.alterar(vcon, emsql)
    if opalter == 2:
        dot()
        tnom = str(input("Digite o Nome: "))
        vsql = f"SELECT * FROM tb_agenda WHERE T_NOME LIKE '{tnom}'"
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
        
        dadoalter = int(input("Alterar:\n1.Nome\n2.Telefone\n3.E-mail\nOpcao: "))

        if dadoalter == 1:
            dot()
            name = str(input("Nome: "))
            newname = str(input("Novo Nome: "))
            namesql = f"UPDATE tb_agenda SET T_NOME='{newname}' WHERE T_NOME LIKE '{name}'"
            suporte.alterar(vcon, namesql)
        if dadoalter == 2:
            dot()
            newtel = str(input("Novo Telefone: "))
            telsql = f"UPDATE tb_agenda SET T_TELEFONE='{newtel}' WHERE T_NOME LIKE '{tnom}'"
            suporte.alterar(vcon, telsql)
        if dadoalter == 3:
            dot()
            em = str(input("E-mail: "))
            newem = str(input("Novo E-mail: "))
            emsql = f"UPDATE tb_agenda SET T_EMAIL='{newem}' WHERE T_EMAIL LIKE '{em}'"
            suporte.alterar(vcon, emsql)
    if opalter == 3:
        dot()
        ttel = str(input("Digite o Telefone: "))
        vsql = f"SELECT * FROM tb_agenda WHERE T_TELEFONE LIKE '{ttel}'"
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
        
        dadoalter = int(input("Alterar:\n1.Nome\n2.Telefone\n3.E-mail\nOpcao: "))

        if dadoalter == 1:
            dot()
            name = str(input("Nome: "))
            newname = str(input("Novo Nome: "))
            namesql = f"UPDATE tb_agenda SET T_NOME='{newname}' WHERE T_NOME LIKE '{name}'"
            suporte.alterar(vcon, namesql)
        if dadoalter == 2:
            dot()
            newtel = str(input("Novo Telefone: "))
            telsql = f"UPDATE tb_agenda SET T_TELEFONE='{newtel}' WHERE T_TELEFONE LIKE '{ttel}'"
            suporte.alterar(vcon, telsql)
        if dadoalter == 3:
            dot()
            em = str(input("E-mail: "))
            newem = str(input("Novo E-mail: "))
            emsql = f"UPDATE tb_agenda SET T_EMAIL='{newem}' WHERE T_EMAIL LIKE '{em}'"
            suporte.alterar(vcon, emsql)
    if opalter == 4:
        dot()
        tem = str(input("Digite o Email: "))
        vsql = f"SELECT * FROM tb_agenda WHERE T_EMAIL LIKE '{tem}'"
        res = suporte.consultar(vcon, vsql)
        dot()
        for dados in res:
            print(dados[1] + "\n" + dados[2] + "\n" + dados[3])
            dot()
        
        dadoalter = int(input("Alterar:\n1.Nome\n2.Telefone\n3.E-mail\nOpcao: "))

        if dadoalter == 1:
            dot()
            name = str(input("Nome: "))
            newname = str(input("Novo Nome: "))
            namesql = f"UPDATE tb_agenda SET T_NOME='{newname}' WHERE T_NOME LIKE '{name}'"
            suporte.alterar(vcon, namesql)
        if dadoalter == 2:
            dot()
            newtel = str(input("Novo Telefone: "))
            telsql = f"UPDATE tb_agenda SET T_TELEFONE='{newtel}' WHERE T_EMAIL LIKE '{tem}'"
            suporte.alterar(vcon, telsql)
        if dadoalter == 3:
            dot()
            em = str(input("E-mail: "))
            newem = str(input("Novo E-mail: "))
            emsql = f"UPDATE tb_agenda SET T_EMAIL='{newem}' WHERE T_EMAIL LIKE '{em}'"
            suporte.alterar(vcon, emsql)
def deleta():
    opdel = int(input("Deletar por:\n1.Nome\n2.Telefone\n3.E-mail\nOpcao: "))

    if opdel == 1:
        dot()
        delname = str(input("Digite o nome: "))
        dlnsql = f"DELETE FROM tb_agenda WHERE T_NOME LIKE '{delname}'"
        suporte.deletar(vcon, dlnsql)
    print("Opcao de Deletar")
def swit(opc):
    if opc == 1:
        dot()
        cadastro()
        os.system("pause")
    elif opc == 2:
        dot()
        consulta()
        os.system("pause")
    elif opc == 3:
        dot()
        altera()
        os.system("pause")
    elif opc == 4:
        dot()
        deleta()
        os.system("pause")
    else:
        dot()
        print("Opcao Invalida")
        os.system("pause")

def main():
    while(True):
        dot()
        print("BANCO DE DADOS - AGENDA")
        dot()
        opc = int(input("1.Cadastrar\n2.Consultar\n3.Alterar\n4.Deletar\n5.Sair\nOpcao: "))
        if opc == 5:
            break
        swit(opc)
        os.system("cls")

main()
vcon.close()
