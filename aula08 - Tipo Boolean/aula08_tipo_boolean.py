aula = True
print(aula)         #True

aula = 10 > 15
print(aula)         #False

aula = ""
print(bool(aula))   #False
if aula:
    print("Possui texto")
else:
    print("Vazio")


aula = "CFB Curso"
if aula:
    print("Possui texto")
else:
    print("Vazio")


aula = 0
print(bool(aula))  #False

aula = 1
print(bool(aula))  #True