opciones = [1,2,3,4]
i = 0
while i < len(opciones):
    opcion = opciones[i]
    if opcion == 1:
        print("Hola mundo")
    elif opcion == 2:
        print("Chao mundo")
    elif opcion == 3:
        print("Paralelepipedo")
    elif opcion == 4:
        print("Adios")
        break
    else:
        print("Fuera del rango ")
    i += 1