contactos = {}
valor = 1
while valor != 0:
    valor = int(input("\nQUE DESEA REALIZAR? \n Añadir/Modificar contacto --> 1 \n Buscar contacto --> 2 \n Borrar contacto --> 3\n Listar contactos --> 4\n Salir --> 0\n Respuesta: "))
    if valor == 1:
        añadiromofificar = int(input("Que desea realizar: \n Añadir --> 1 \ Modificar --> 2\n"))
        if añadiromofificar == 1:
            contacto1 = input("Ingrese nombre del contacto: ")
            contacto2 = int(input("Ingrese número: "))
            contactos.update({contacto1: contacto2})
        elif añadiromofificar == 2:
            print(contactos)
            contacto1 = str(input("Ingrese el nombre del contacto: "))
            contacto2 = str(input("Ingrese otro número: "))
            contactos[contacto1] = contacto2
            print(contactos)
    elif valor == 2:
        print("BUSCAR CONTACTO!!!")
        buscar1 = input("ingrese el nombre del contacto que desea buscar: ")
        if buscar1 in contactos:
            print("Ese contacto es: ", buscar1, ", Con número:", contactos[buscar1] )
        else:
            print("no existe ese contacto... :(")
    elif valor == 3:
        print("CONTACTOS: ")
        for i in contactos:
            print(i,":", contactos[i])
        contacto1 = input("Qué contacto desea eliminar?: ")
        if contacto1 in contactos:
            contactos.pop(contacto1)
            print(contactos)
        else:
            print("no existe ese contacto....")
    elif valor == 4:
        for i in contactos:
            print(i,":", contactos[i])
    elif valor == 0:
        print("Vale gracias.")
    else: 
        print("No hay ninguna opción con ese valor")
        valor = 1
