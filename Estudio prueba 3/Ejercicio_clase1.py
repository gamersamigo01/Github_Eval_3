si_veterinaria = False
perro = gato = loro = pato = otros = 0
cantidad_animales = 0
while not si_veterinaria:
    print("1. Ingresar cantidad")
    print("2. Ingresar animales")
    print("3. Salir")
    opcion = int(input("Ingrese la opcion: "))

    if opcion ==  1:
        cantidad_valida = False
        while not cantidad_valida:
            try:
                cantidad_animales = int(input("Ingrese cuantos animales va a ingresar: "))
            except ValueError:
                print("Error, ingrese un numero entero")
            else:
                if cantidad_animales > 0:
                    print("Cantidad ingresada")
                    cantidad_valida = True
                else:
                    print("Error, tiener que ser un numero mayor a 0")
    elif opcion == 2:
        if cantidad_animales == 0:
            print("no ha ingresado cantidad, ingrese a la pirmera opcion y despues vuelva")
        else:
            for animal in range(cantidad_animales):
                try:
                    animal_ing = input("Ingrese el animal: ").strip().lower()
                except ValueError:
                    print("Error,ingrese nuevamente")
                else:
                    nombre_valido = False
                    while not nombre_valido:
                        nombre = input("Ingrese el nombre del animal: ").strip().lower()
                        if len(nombre) >= 3 and not nombre.isdigit():
                            print("Nombre ingresado correctamente")
                            nombre_valido = True
                        else:
                            print("Error, el nombre debe tener mas de 3 caracteres")
                        
    elif opcion == 3:
        print("Adios")
        si_veterinaria = True
    else:
        print("Error, opcion fuera del rango")