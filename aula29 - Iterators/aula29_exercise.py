def ContadorPersonalizado(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(c)

ini = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
ContadorPersonalizado(ini, fim, passo)