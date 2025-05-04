import os
carros = []
class Carro:
    nome = ""
    potencia = 0
    velMax = 0
    ligado = False 
    def  __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velMax = int(potencia)*2
        self.ligado = False 
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def info(self):
        print("Nome: " + self.nome)
        print("Potencia: " + str(self.potencia))
        print("Vel.Max: " + str(self.velMax))
        print("Ligado: " + ("Sim" if self.ligado==True else "Nao"))
        print("----------------------------")

def menu():
    os.system("cls") or None
    print("1.Novo Carro")
    print("2.Informacoes do Carro")
    print("3.Excluir Carro")
    print("4.Ligar Carro")
    print("5.Desligar Carro")
    print("6.Listar Carros")
    print("7.Quantidade de Carros")
    print("8.Sair")
    opc = input("Opcao: ")
    return opc
def novoCarro(new):
    name = str(input("Nome do carro: "))
    pot = int(input("Potencia: "))
    new = Carro(name, pot)
    carros.append(new)
    os.system("pause")
def ordem():
    pos = int(input("Posicao: "))
    try:
        carros[pos].info()
    except:
        print("Carro nao esta na lista")
    os.system("pause")
def excluir():
    pos = int(input("Posicao: "))
    for c in range(len(carros)):
        if c == pos:
            carros.pop(c)
    os.system("pause")   
def ligarCarro():
    pos = str(input("Nome: "))
    for c in carros:
        if c == pos:
            c.ligar()
    os.system("pause")
def desligarCarro():
    pos = str(input("Nome: "))
    for c in carros:
        if c == pos:
            c.desligar()
    os.system("pause") 
def listar():
    for c in range(len(carros)):
        carros[c].info()
    os.system("pause")
def quant():
    print(len(carros))
    os.system("pause")

def switch_case(opc):
    match opc:
        case 1:
            new = str(input("Novo Carro: "))
            return novoCarro(new)
        case 2:
            return ordem()
        case 3:
            return excluir()
        case 4:
            return ligarCarro()
        case 5:
            return desligarCarro()
        case 6:
            return listar()
        case 7:
            return quant()

ret = menu()
while int(ret) < 8:
    switch_case(int(ret))
    ret = menu()
