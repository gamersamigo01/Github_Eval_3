sum_pesado = sum_liviano = 0
placa_valida = True
try:
    cuant_auto = int(input("Ingrese cuantos autos quiere ingresar al programa: "))
except ValueError:
    print("Cantidad invalida!, Ingrese un entero positivo para continuar")
else:
    if cuant_auto > 0:
        for auto in range(0,cuant_auto):
            while placa_valida and auto <= cuant_auto:
                placa = input(f"Ingrese la placa del {auto+1}° auto: ")
                if (len(placa) >= 6) and not (" " in placa):
                    auto += 1
                    print(f"Placa valida {placa}")
                    placa_valida = False
                else:
                    placa = input("Error, Ingrese nuevamente la placa:")
                    placa_valida = True

        for capacidad in range(0,cuant_auto):
            capacidad_auto = int(input(f"Ingrese la capacidad del {capacidad+1}° auto: "))
            if capacidad_auto > 0:
                print(f"Capacidad registrada")  
                if capacidad_auto > 55:
                    sum_pesado += 1
                elif capacidad_auto <= 55:
                    sum_liviano += 1
            else: 
                print("Error, la capacidad debe ser mayor a 0") 
    else:
        print("Error, tiene que ser mayor que cero")
    print(f"La flota cuenta con {sum_pesado} vehiculos pesados y {sum_liviano} vehiculos livianos! ¡Rutas asignadas!")  
