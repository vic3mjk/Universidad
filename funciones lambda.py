cubo = lambda x : x** 3

print(cubo(2))
lista  = [lambda x : x ** 2, lambda x : x ** 0.5]
for numero in lista:
    print(numero(9))