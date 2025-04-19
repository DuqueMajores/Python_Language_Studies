carros_l = ["HRV", "GOLF", "FOCUS", "ARGO"] # Lista

carros_t = ("HRV", "GOLF", "FOCUS", "ARGO") # Tupla

carros_m = [["Modelo", "HRV"], ["Fabricante", "Honda"], ["Ano", 2016]] # Matriz

print(carros_m[0][0])

carros_m[2][1]= 2019

carros_m.append(["Cor", "Prata"])

for l, c in carros_m:
    print(l + " - " + str(c))