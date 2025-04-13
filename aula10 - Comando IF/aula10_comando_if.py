# Desafio: Sistema de Classificação Escolar

def dot():
    print("-------------------------")
def med(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media
def cond(media):
    if(media >= 9.0):
        print("Situação: Melhor Aluno Aprovado!")
    elif(media >= 7.0 and media < 9.0):
        print("Situação: Aprovado")
    elif(media >= 5.0 and media < 7.0):
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")     
def show(nome, n1, n2, n3):
    dot()
    print("Nome do aluno: ", nome)
    print("Nota da primeira prova: ", n1)
    print("Nota da segunda prova: ", n2)
    print("Nota da terceira prova: ", n3)

sys = True
while(sys):
    nome = input(str("Nome: "))
    n1 = float(input("Primeira Nota: "))
    n2 = float(input("Segunda Prova: "))
    n3 = float(input("Terceira Prova: "))

    show(nome, n1, n2, n3)
    media = med(n1, n2, n3)
    print("Média Final: ", media)
    condicao = cond(media)

    dot()

    op = str(input("Continuar [s/n]: "))
    if(op == "s"):
        continue
    elif (op == "n"):
        sys = False
        break
    else:
        print("Erro")
        continue