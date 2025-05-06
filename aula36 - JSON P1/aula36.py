import json
import os

def dot():
    print("------------------------------------")

with open('C:/Users/Admin/Desktop/Cursos/Phyton/Aulas/aula36 - JSON P1/db.json') as f:
    livros=json.load(f)

#chaves
#for chaves in livros["livros"]:
    #print(chaves)

dot()
#itens
#for itens in livros.items():
    #print(itens)

dot()
#valores
#for valores in livros.values():
    #print(valores)

dot()
#nome do livro
#for titulo in livros["livros"]:
    #print(titulo["titulo"])

dot()
#imagens
#for img in livros["livros"]:
    #print(img["imgCapa"])

dot()
#autores
#for autor in livros["livros"]:
    #print(autor["autores"]["autor1"])

dot()
#completo
for livro in livros["livros"]:
    print(
    "Titulo: " + livro["titulo"] +
    "\nAutor: " + ", ".join(livro["autores"]) +  # Supondo que seja uma lista de autores
    "\nCategoria: " + livro["categoria"] +
    "\nISBN: " + str(livro["isbn"]) +
    "\nAno de Publicacao: " + str(livro["ano"]) +
    "\nQuant. Paginas: " + str(livro["paginas"]) +
    "\nPreco: " + str(livro["preco"]) +
    "\nEstoque: " + str(livro["estoque"])
    )
    dot()

dot()
os.system("pause")
