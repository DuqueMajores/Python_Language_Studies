pessoa = {"Nome":"Moises", "Altura":1.70, "Peso":65.0, "Idade":28}

print(pessoa["Nome"])

print(pessoa.keys())

print(len(pessoa))

pessoa["Profissao"] = "Estudante"

pessoa.pop("Altura")

for k in pessoa:
    print(k, "-", pessoa[k])


pessoas = {"Pessoa1":{"Nome":"Caio", "Idade":28},
           "Pessoa2":{"Nome":"Moises", "Idade":29}}


print(pessoas["Pessoa2"]["Nome"])
pessoas["Pessoa3"] = {"Nome":"Luana", "Idade":35}

print(pessoas)

for k in pessoas:
    print(k, "")
    for v in pessoas[k]:
            print(v, "-", pessoas[k][v])
