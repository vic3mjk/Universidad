def factorial (a):
    valor = 1
    for i in range(1, a + 1):
        valor = i * valor
    return valor
print(factorial(int(input("ingres enumero para calcular su factorial: "))))