sum_pesado = sum_liviano = 0
placa_valida = True
try:
    cuant_auto = int(input("Ingrese cuantos autos quiere ingresar al programa: "))
except ValueError:
    print("Cantidad invalida!, Ingrese un entero positivo para continuar")
else:
    if cuant_auto > 0:
        for auto in range(cuant_auto):
            while True:
                placa = input(f"Ingrese la placa del {auto+1}° auto: ")
                if (len(placa) >= 6) and not (" " in placa):
                    print(f"Placa valida {placa}")
                    break
                else:
                    print("Error, la placa tiene que tener al menos 6 caracteres y no tener espacios")
                    
            while True:
                try:
                    capacidad_auto = int(input(f"Ingrese la capacidad del {auto+1}° auto: "))
                except ValueError:
                    print("Error, ingrese un numero entero positivo")
                else:
                    if capacidad_auto > 0:
                        print(f"Capacidad registrada")  
                        if capacidad_auto > 55:
                            sum_pesado += 1
                        else:
                            sum_liviano += 1
                        break
                    else: 
                        print("Error, la capacidad debe ser mayor a 0") 
    else:
        print("Error, tiene que ser mayor que cero")
    print(f"La flota cuenta con {sum_pesado} vehiculos pesados y {sum_liviano} vehiculos livianos! ¡Rutas asignadas!")  
