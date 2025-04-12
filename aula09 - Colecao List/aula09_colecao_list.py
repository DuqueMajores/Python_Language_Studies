carros = ["HRV", "Golf", "Argo", "Focus"]
print(carros)
carros[3] = "Fusion"

print(carros[0])
print(carros[-1]) #mostra o ultimo

carros.append("Fit") #Adiciona a lista
carros.append("Focus")
carros.append("Polo")

print(carros)
print(str(len(carros)) + " carros na lista ")

carros.remove("Fusion") # Remove o elemento
print(carros)
print(str(len(carros)) + " carros na lista ")

carros.pop() #Remove o ultimo elemento
print(carros)
print(str(len(carros)) + " carros na lista ")

del carros[2] #remove na posicao desejada
print(carros)
print(str(len(carros)) + " carros na lista ")


carros2 = list(carros) #carros2 recebe a lista carros
print(carros2)
print(str(len(carros2)) + " carros na lista ")


carros2 = ["Fusca", "147", "Brasilia", "Celta"]

carros3 = carros + carros2
print(carros3)
print(str(len(carros3)) + " carros na lista ")

carros.clear() #limpa a lista
print(carros)
print(str(len(carros)) + " carros na lista ")