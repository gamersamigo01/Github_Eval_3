print("Bienvenido a cafeteria universitaria")
caja_chica = 150_000
gasto_neto = 0
menu_bool = False
while not menu_bool:
    print("1. Ver saldo actual en caja")
    print("2. Registrar egreso(Gasto de insumos)")
    print("3. Registrar ingreso(Reposición de fondos)")
    print("4. Ver balance neto de movimientos")
    print("5. Cerrar caja y salir")
    try:
        opt = int(input("Ingrese la opcion: "))
    except ValueError:
        print("Error, ingrese un numero entero")
    else:
        if opt == 1:
            print(f"Saldo en caja: {caja_chica}")
        elif opt == 2:
            egreso_comprobante = False
            while not egreso_comprobante:                
                try:
                   egreso = int(input("Ingrese cuanto se egreso de caja: "))
                except ValueError:
                   print("Error, ingrese un numero entero")
                else:   
                    if egreso > 0 and egreso <= caja_chica:
                        caja_chica -= egreso
                        gasto_neto -= egreso
                        print("Egreso confirmado")
                        egreso_comprobante = True
                    else:
                        print("Error, tiene que tener un valor mayor a 0 y menor al total de la caja chica")
        elif opt == 3:
            ingreso_comprobante = False
            while not ingreso_comprobante:
                try:
                    ingreso = int(input("Ingrese cuanto se ingreso a la caja: "))
                except ValueError:
                    print("Error, ingrese un numero entero")
                else:
                    if ingreso > 0 and ingreso + caja_chica <= 500_000:
                        caja_chica += ingreso
                        gasto_neto += ingreso
                        print("Ingreso comprobado")
                        ingreso_comprobante = True
                    else:
                        print("Error, el valor debe ser mayor a 0 y no superar los 500.000 en caja")
        elif opt == 4:
            print(f"Balance acomulado de hoy: ${gasto_neto}")
        elif opt == 5:
            print("Gracias por usar el programa, adios")
            menu_bool = True
        else:
            print("error, Ingrese una opcion del 1 al 5")
        
                    