#lista super
sw = 1
lista_super = []
valor_super = []
print("Precione 1 para ingresar los productos del super")
print("Precione cualquier tecla para salir")

opt = input("Ingrese su opcion: ")

if opt == "1":
    while sw ==1:
        try:
            print("-"*16)
            producto = input("Ingrese sus productos, para salir ingrese 0: ")
            if producto != "0":
                lista_super.append(producto)
                valor_producto = int(input("Ingrese el valor del (producto): "))
                valor_super.append(valor_producto)
                print("----DETALLE DE LA BOLETA----")
                print(f"Sus productos son: {lista_super}")
                print(f"Usted ingreso: {len(lista_super)} productos")
                print(f"El precio total es de: {sum(valor_super)}")
            else:
                print("Gracias")
                sw = 0
        except:
            print("Ingreso erroneo")
else:
    print("Adios")
    