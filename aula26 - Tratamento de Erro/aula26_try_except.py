try:
    print(x)
except:
    print("X nao foi definido")
else:
    print("Sem erros")
finally:
    print("Saindo do teste...")


num = 10 
if num < 1:
    raise Exception("Valor nao permitido")

num1 = 10
if not type(num1) is int:
    raise Exception("Somante numeros permitidos")
else:
    print(str(num1) + " - Valor valido")
