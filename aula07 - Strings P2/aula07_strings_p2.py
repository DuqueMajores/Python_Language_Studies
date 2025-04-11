#In and Not In

curso = "Curso de Python"
palavra = "curso"

res = "Python" in curso # x está em y?
print(res)
res = "Python" not in curso #Nao esta?
print(res)

res = palavra in curso
print(res)
res = palavra.upper() in curso.upper()
print(res)

#---------------------------------------
#Concatenação

curso = "Curso de Python"
canal = "CFB Cursos"

res = curso + " do canal " + canal
print(res)

cidade = "Belo Horizonte"
dia = 15
mes = "Dezembro"
ano = 2019

print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano))

# OU

data = "{}, {} de {} de {}"
print(data.format(cidade, dia, mes, ano))

# OU

print("{}, {} de {} de {}".format(cidade, dia, mes, ano))

#---------------------------------------
# Escape

print("Esta frase corta \na linha")

print("\"Aspas\"")

# \' - Aspas simples
#\"" - Aspas duplas
#\r - Enter
#\t - Tabulação
#\b - BackSapce