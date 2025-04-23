soma = lambda a, b: a + b
print(soma(2, 5))

mult = lambda a, b, c: (a + b)*c
print(mult(2, 3, 5))

print((lambda a, b: a + b)(3, 2))

r = lambda x, func: x + func(x)
res = r(2, lambda x: x*x)
print(res)