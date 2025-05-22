diccionario ={"janara":"teamo",
              "elpepe": "teodio"}
valoxd= input("ingrese un nombre:v:  ")
num = (int(input("ingrese un numero: ")))
diccionario[valoxd] = num
print(diccionario)
valor = 0
while valor == 0:
    buscar = (input("cuál es tu nommbre( pon janara solo confifure eso jaja): "))
    if buscar in diccionario.keys():
        print(diccionario.values())
        valor = 1
    else:
        print("NOMBRE NO INGRESADO")
        valor = 0

