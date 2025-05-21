numero = int(input("Ingrese número: "))
verificador = lambda x : "positivo" if x > 0 else "negativo" if x < 0 else "cero"
print(f"el numero es {verificador(numero)}")