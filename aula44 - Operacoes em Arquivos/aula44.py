import re
import os

#Criando, abrindo e deletando arquivos
nome = "teste.txt"
caminho = "C:/Users/Admin/Desktop/Cursos/Phyton/Aulas/aula44"

#r - read Leitura
#a - append Anexar
#w - write Escrita ou Cria
#x - create Criar
#t - texto
#b - binario

#file.write("CFB Cursos")

if os.path.exists(caminho+nome):
    os.remove(caminho+nome)
    print("Arquivo removido")
else:
    file = open("C:/Users/Admin/Desktop/Cursos/Phyton/Aulas/aula44"+ nome, "x")
    file.close()
    print("Arquivo criado")
    

