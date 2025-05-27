def valortotal(valor_diario, cantidad_dias):
    return valor_diario * cantidad_dias

valor3 = "si"
diccionario = {}
for i in range(1, 21):
    diccionario[i] = "libre"
diccionario1 = {}
for i in range(1, 21):
    diccionario1[i] = "libre"
diccionario2 = {}
for i in range(1, 21):
    diccionario2[i] = "libre"

while valor3 == "si":
    cabana = [[1, 2, 3], [10000, 20000, 30000]]
    valor = 0
    while valor == 0:
        eleccion = int(input(("Elija su cabaña:\n 1 (1 Persona, Valor = $10000)\n 2 (2 Personas, Valor = $20000)\n 3 (3 Personas, Valor = $30000)\n: ")))
        if eleccion == 1 or eleccion == 2 or eleccion == 3:
            valor = 1

    valor5 = "si"
    while valor5 == "si":
        while eleccion > 0 and eleccion <= 3:
            if eleccion in cabana[0]:
                if eleccion == 1:
                    print(f"valor por día es {cabana[1][eleccion - 1]}")
                    diainicial = int(input("ESCOJA EL DIA INICIAL: "))
                    diafinal = int(input("escoja el dia final: "))
                    cantidad_dias = diafinal - diainicial + 1
                    if "Ocupado" in diccionario[diainicial]:
                        print("Esta cabaña está ocupada")
                    elif "libre" in diccionario[diainicial]:
                        for i in range(diainicial, diafinal + 1):
                            diccionario[i] = "Ocupado"
                        print(diccionario)
                        total = valortotal(cabana[1][eleccion - 1], cantidad_dias)
                        print(f"Total a pagar: ${total}")

                elif eleccion == 2:
                    print("valor por día: 20000")
                    diainicial = int(input("ESCOJA EL DIA INICIAL: "))
                    diafinal = int(input("escoja el dia final: "))
                    cantidad_dias = diafinal - diainicial + 1
                    if "Ocupado" in diccionario1[diainicial]:
                        print("Esta cabaña está ocupada")
                    elif "libre" in diccionario1[diainicial]:
                        for i in range(diainicial, diafinal + 1):
                            diccionario1[i] = "Ocupado"
                        print(diccionario1)
                        total = valortotal(cabana[1][eleccion - 1], cantidad_dias)
                        print(f"Total a pagar: ${total}")

                elif eleccion == 3:
                    print("valor por dia es 30000")
                    diainicial = int(input("ESCOJA EL DIA INICIAL: "))
                    diafinal = int(input("escoja el dia final: "))
                    cantidad_dias = diafinal - diainicial + 1
                    if "Ocupado" in diccionario2[diainicial]:
                        print("Esta cabaña está ocupada")
                    elif "libre" in diccionario2[diainicial]:
                        for i in range(diainicial, diafinal + 1):
                            diccionario2[i] = "Ocupado"
                        print(diccionario2)
                        total = valortotal(cabana[1][eleccion - 1], cantidad_dias)
                        print(f"Total a pagar: ${total}")
                else:
                    print("número no ingresado")
                eleccion = 33333
            valor5 = "no"
    valor3 = input("Desea seguir arrendando una cabaña?: si/no: ")
