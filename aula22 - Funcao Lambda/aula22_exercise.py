calcular_bonus = lambda salarios: [
    salario * 0.20 if salario < 3.000 else salario * 0.10 for salario in salarios
]

print(calcular_bonus([2500, 3200, 2800, 4000]))
