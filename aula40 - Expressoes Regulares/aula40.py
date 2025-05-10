import re

def dot():
    print("-----------------------------------")

texto = "Texto teste para RegEx Python"

#RegEx findall - Colecao das ocorrencias encontradas

#res = re.findall("Python", texto)
#print(res) #['Python']

#res = re.findall("e", texto)
#print(res) #['e', 'e', 'e', 'e']
#print(len(res))

#pesq = input("Pesquisar: ")
#res = re.findall(pesq, texto)
#print(res)

#for i in res:
    #print(i)

dot()

#RegEx search - Indica a posicao encontrada

#pesq = input("Pesquisar: ")
#res = re.search(pesq, texto)
#print(res.start())

dot()

#RegEx split - Onde encontar a ocorrencia, splita

#res = re.split("e", texto)
#print(res)

#for i in res:
    #print(i)

dot()

#RegEx sub - Retorna a sting substituida

res = re.sub("\s", ".", texto)
res = re.sub("r", "l", res)
print(res)
