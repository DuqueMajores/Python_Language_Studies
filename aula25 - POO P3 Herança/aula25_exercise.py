class Funcionario:
    nome = ""
    cargo = ""
    salario = 0
    def __init__(self, n, c, s):
        self.nome = n
        self.cargo = c
        self.salario = s
    def info(self):
        print("Nome.....: " + self.nome)
        print("Cargo....: " + self.cargo)
        print("Salario..: " + str(self.salario))
        print("----------------------")


f1 = Funcionario("Moises", "Gerente", 3500)
f1.info()
