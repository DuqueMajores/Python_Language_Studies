def somar(*num):
    res = 0
    for n in num:
        res += n
    print(f"A soma dos valores: {res}")

somar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def textos(*txt):
    for t in txt:
        print(t)

textos("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

def carro(c="Golf"):
    print(c)

carro("HRV")
carro()