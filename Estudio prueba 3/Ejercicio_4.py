print("Bienvenido al control de fondos, la caja chica tiene un fondo de 150.000 en principio")
caja_chica = 150000
menu_comprobador = False
balance_movimientos = 0
while not menu_comprobador:
    print("1. Ver saldo actual en caja")
    print("2. Registrar egresos(Gasto de insumos)")
    print("3. Registrar ingreso(Reposicion de fondos)")
    print("4. Ver balance neto de movimientos")
    print("5. Cerrar caja y salir")
    try:
        opt = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Error, ingrese un numero entero")
    else:
        if opt == 1:
            print(f"La caja tiene un saldo de: {caja_chica}")
        elif opt == 2:
            egreso_correcto = False
            while not egreso_correcto:  
                try:
                    egreso = int(input("Ingrese el monto de egreso: "))
                except ValueError:
                    print("Error, ingrese un numero entero")
                else:
                    if egreso > 0:
                        if egreso <= caja_chica:
                            caja_chica -= egreso
                            balance_movimientos -= egreso
                            print("Se a descontado de la caja") 
                            egreso_correcto = True
                        else:
                            print("El egreso no puede ser mayor al total de caja")
                    else:
                        print("Error, tiene que egresar un valor mayor a 0")
        elif opt == 3:
            ingreso_correcto = False
            while not ingreso_correcto:
                try:
                    ingreso = int(input("Ingrese el monto a ingresar: "))
                except ValueError:
                    print("Error, ingrese un numero entero")
                else:
                    if ingreso > 0:
                        caja_chica += ingreso
                        if caja_chica <= 500000:
                            print("Cantidad ingresada con exito")
                            balance_movimientos += ingreso
                            ingreso_correcto = True
                        else:
                            print("La cantidad maxima que se puede ingresar a la caja es de 500.000, no se puede exeder")
                        print("Error, Tiene que ingresar un valor mayor a 0")
        elif opt == 4:
            print(f"[flujo neto] El balance de movimientos de hoy es de: ${balance_movimientos}")
        elif opt == 5:
            print("Gracias por usar este programa")
            menu_comprobador = True
        else:
            print("Error, no esta dentro de los parametros del menu")    
                                                       