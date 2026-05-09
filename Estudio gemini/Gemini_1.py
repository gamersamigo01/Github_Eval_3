print("Calculador de notas")
print("Ingrese 1 para anotar las notas")
print("Ingrese cualquier otra tecla para salir")
sw = 1
notas = []

opt = input("Ingrese su opcion: ")

if opt == "1":
    while sw == 1:
        try:
            nota = float(input("Ingrese sus notas, para salir ingrese 0: "))
            if nota != 0:
                notas.append(nota)
                print(f"Sus notas: {notas}")
                print(f"Cuantas notas lleva: {len(notas)}")
                print(f"Promedio de notas: {sum(notas) / len(notas)}")
            else:
                print("Adios")
                sw = 0
        except:
            print("Error")
else:
    print("Adios")
