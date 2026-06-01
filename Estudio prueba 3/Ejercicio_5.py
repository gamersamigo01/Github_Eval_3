maleta_comprobacion = False
cuant_maletas = 0
sobrepeso = estandar = 0
while not maleta_comprobacion:
    try:
        cuant_maletas = int(input("Ingrese cuantas maletas va a ingresar: "))
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    else:
        if cuant_maletas > 0:
            print("maletas ingresadas")
            maleta_comprobacion = True
        else:
            print("Error, deber ingresar al menos una maleta")
for maleta in range(cuant_maletas):
    codigo_comprobacion = False
    while not codigo_comprobacion:
        try:
            codigo_barra = input(f"Ingrese el codigo de su codigo de barras de su {maleta+1}° maleta: ").strip().lower()
        except ValueError:
            print("Error, ingrese un valor aceptable")
        else:
            if (len(codigo_barra) >= 7) and not (" " in codigo_barra):
                print("Codigo de maleta ingresado")
                codigo_comprobacion = True
            else:
                print("Error, el codigo debe tener al menos 7 caracteres y no tener espacios intermedios")
    peso_comprobacion = False
    while not peso_comprobacion:
        try:
            peso_maleta = int(input(f"Ingrese el peso de su {maleta+1}° maleta: "))
        except ValueError:
            print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga")
        else:
            if peso_maleta > 0:
                print("peso registrado")
                peso_comprobacion = True
            else:
                print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga")
        if peso_maleta > 23:
            sobrepeso += 1
        else:
            estandar += 1
print(f"Sus maletas cuenta con {sobrepeso} maletas con sobrepeso y {estandar} con peso estandar")
            
        
