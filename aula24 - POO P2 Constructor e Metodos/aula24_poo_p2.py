class Carro:
    velMax = 0
    ligado = False
    cor = ""

    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    def mostrar(self):
        print(self.velMax)
        print(self.ligado)
        print(self.cor)

    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    

c1 = Carro(200, False, "Preto")
c2 = Carro(20, False, "Branco")
c3 = Carro(350, False, "Vermelho")

c1.ligar()

c1.mostrar()
