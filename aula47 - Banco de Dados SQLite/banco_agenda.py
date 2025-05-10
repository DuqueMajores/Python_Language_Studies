import conexao_e_manipulacao
import os

vcon = conexao_e_manipulacao.conexaoBanco()

### Criando Tabela
tabelasql = """CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""
#conexao_e_manipulacao.criarTabela(vcon, tabelasql)

#----------------------------------------------

### Inserindo Dados
"""while(True):
    try:
        nome = str(input("Nome: "))
        telefone = input("Telefone: ")
        email = str(input("E-mail: "))
    except ValueError as err:
        print(err)
    
    dadosql = f(x3")INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
            VALUES('{nome}', '{telefone}', '{email}')(x3")

    conexao_e_manipulacao.inserir(vcon, dadosql)

    loop = str(input("Continuar? [s/n]: "))
    if loop == "n" or loop == "N":
        break
    else:
        continue"""

#--------------------------------------------------

### Deletando Registro da Tabela
"""dadosql = "DELETE FROM tb_contatos WHERE N_IDCONTATO=1"

conexao_e_manipulacao.deletar(vcon, dadosql)"""

#---------------------------------------------------

### Atualizando Registro
dadosql = "UPDATE tb_contatos SET T_NOMECONTATO='Bruno', T_TELEFONECONTATO='2199999999', T_EMAILCONTATO='bruno@gmail.com' WHERE N_IDCONTATO=2"

#conexao_e_manipulacao.atualizar(vcon, dadosql)

#---------------------------------------------------

### Consultando Registro
dadosql = "SELECT * FROM tb_contatos"
#"SELECT tb_contatos WHERE T_NOMECONTATO LIKE 'A%'"

res = conexao_e_manipulacao.consultar(vcon, dadosql)

for dados in res:
    print(str(dados[0]) + "." + dados[1] + " - " + dados[2] + " - " + dados[3] )

#---------------------------------------------------

os.system("pause")

vcon.close()
