#Promedio notas
sw = 1
lista_notas = []

print("Presione 1 para ingresar sus notas")
print("Presiones cualquier tecla para salir")
opt= int(input("Ingrese su opcion: "))

if opt == 1:
    while sw==1:
        try:
            print("-"*16)
            nota = int(input("Ingrese su nota, si desea salir precione 0: "))
            if nota != 0:
                lista_notas.append(nota)
                print(f"Su lista de notas es: {lista_notas}")
                print(f"Cantidad de notas cargadas: {len(lista_notas)}")
                print(f"Su promediode notas es: {sum(lista_notas) / len(lista_notas)}")
                    
            else:
                print("Adios")
                sw = 0
        except:
            print("Ingreso erroneo")
else:
    print("Adios")