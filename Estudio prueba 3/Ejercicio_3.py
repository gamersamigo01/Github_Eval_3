temp_alta = 0
temp_normal = 0
temp_sensor = 0
while True:
    try:
        cant_sensores = int(input("Ingrese la cantidad de lecturas que quiere hacer: "))
    except ValueError:
        print("Error, ingrese un numero entero")
    else:
        if cant_sensores > 0:
            break
        else:
            print("Error, el numero tiene que ser mayor a 0")
for sensor in range(cant_sensores):
    while True:
        try:
            codigo_sensor = input(f"Ingrese el codigo del sensor {sensor+1}: ")
        except ValueError:
            print("Ingrese un valor valido")
        else:
            if len(codigo_sensor) >= 5 and " " not in codigo_sensor:
                print(f"{sensor+1}° codigo de sensor agregado")
                break            
            else:
                print("Error, tiene que tener una longitud mayor a 4 y no contener ningun espacio")
    while True:
        try:
            temp_sensor = int(input(f"Ingrese la temperatura del {sensor+1} sensor: "))
        except ValueError:
            print("Error, tiene que ser un numero entero")
        else:
            if temp_sensor >= -10 and temp_sensor <= 50:
                print(f"{sensor+1}° Temperatura ingresada")
                break
            else:
                print("Error, la temperatura debe ser mayor a -10° grados y menor a 50°")
    if temp_sensor > 30:
        temp_alta += 1
    else:
        temp_normal += 1
print(f"El invernadero registró {temp_alta} lecturas altas y {temp_normal} lecturas normales, ajuste de ventilacion ejecutado")