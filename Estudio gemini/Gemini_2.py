lista_animales = []
cantidad_animales = []
sw = 1

print("Registro de animales")
print("Para ingresar los animales introdusca 1, si desea salir presione cualquier otra tecla")
opt = input("Ingrese su opcion: ")

if opt == "1":
    while sw == 1:
        try:
            print("Ingrese el animal, si quiere salir ingrese 0")
            animal = input("Animal: ")           
            if animal != "0":
                cuantos = int(input("Ingrese cuantos animales hay de este tipo: "))
                lista_animales.append(animal)
                cantidad_animales.append(cuantos)
                print(f"Lista de animales: {lista_animales}")
                print(f"Cuantos animales lleva: {sum(cantidad_animales)}")
            else:
                print("Adios")
                sw = 0
        except:
            print("Error: ingrese una cantidad numerica valida")
else:
    print("adios")