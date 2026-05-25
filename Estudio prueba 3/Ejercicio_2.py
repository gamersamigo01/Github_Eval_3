print("¡Bienvenido al sistema de gestion de localidades del teatro municipal!")

suma_neta = 0
suma_localidades = 200
while True:
    print("Elija una opcion")
    print("1. Localidades disponibles")
    print("2. Vender localidades")
    print("3. Devolver localidades")
    print("4. Historial de ventas")
    print("5. Salir")
    try:
        opt = int(input("Opcion: "))
    except ValueError:
        print("Error, escriba un numero entero positivo")
    else:
        if opt == 1:
            print(f"Quedan: {suma_localidades} localidades")
        elif opt == 2:
            try:
                cuant_localidad = int(input("Ingrese cuantas localidades va vender: "))
                if cuant_localidad < suma_localidades and cuant_localidad > 0:
                    suma_localidades -= cuant_localidad
                    suma_neta += cuant_localidad
                    print("Localidades vendidas con exito")
                else:
                    print("Error, Las propiedades en ventas deben ser mayor a 0 y menor al total de localidades disponibles")
            except ValueError:
                print("Error, Ingrese un numero entero")
        elif opt == 3:
            try:
                cuant_localidad = int(input("Ingrese cuantas propiedades quiere devolver: "))
                if cuant_localidad > 0 and cuant_localidad <= suma_localidades:
                    suma_localidades += cuant_localidad
                    suma_neta -= cuant_localidad
                else:
                    print("Error, tiene que ser mayor a 0 y debe ser menor al total de localidades")
            except ValueError:
                print("Error, Ingrese un numero entero")
        elif opt == 4:
            print(f"Se vendieron {suma_neta} propiedades neto")
        elif opt == 5:
            print("gracias por usar el programa")
            break
        else:
            print("Error, no puede ser un numero menor o igual a 0")

