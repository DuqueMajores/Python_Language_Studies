valores = [1, 2, 3, 4, 5]

def somar(num):
    res = 0
    for n in num:
        res += n
    return res

print(somar(valores))

def vallista(*num):
    for v in num:
        print(f"{v} , ")

print(f"A soma de {vallista(valores)} e igual a: {str(somar(valores))}")