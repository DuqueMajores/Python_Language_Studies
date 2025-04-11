#Localização e Tamanho

curso = "Curso de Python"

print(curso) #Curso de Python
print(curso[0]) #C
print(curso[0:5]) #Curso
print(curso[9:15]) #Python

print("Tamanho:", len(curso)) #tamanho

#---------------------------------------
#Manipulação de Texto

curso = " Curso de Python "

print(curso.strip()) #Tira os espaços
print(curso.lower()) #Converte para minusculo
print(curso.upper()) #Converte para maiusculo

#---------------------------------------
#Corte

curso = "Curso de Python"

print(curso.replace("Python", "C++")) #Substitui

a = curso.split(" ") #Faz um corte 
print(a[0]) #Curso
print(len(a)) #3



#---------------------------------------
# EXEMPLO - Capturar Sobrenome

print("#---------------------------------------")

nome = input("Digite seu nome todo: ")
palavras = nome.split()
print("Seu ultimo nome é: ", palavras[len(palavras) -1])

