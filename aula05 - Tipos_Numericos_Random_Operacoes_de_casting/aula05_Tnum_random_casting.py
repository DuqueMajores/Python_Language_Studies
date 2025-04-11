import random

#Tipos Numericos

num_i = 10 #type - int
num_f = 5.2 #type - float
num_c = 1j #type - complex

x = int(num_f) #parte inteira
x = float(num_i) #torna-se float

print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

#Numeros Aleatorios (Random)

num = [
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59), 
    ] #Lista / Array

print(num)