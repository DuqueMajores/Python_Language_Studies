class Carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro()
c2 = Carro()

c1.velMax = 200
c1.cor = "Preto"
c1.ligado = True

print(c1.velMax)
print(c1.cor)
print(c1.ligado)

estado = "Sim" if c1.ligado else "Nao"
print(estado)