colores = ["rojo","verde","amarillo","morado","negro","azul"]
valor_encontrado = False

color_a_buscar = input("Ingrese un color: ").lower().strip()
for indice,color in enumerate(colores):
    if color == color_a_buscar:
        print(f"{indice+1}- El color es: {color}")
        valor_encontrado = True
        break           
if not valor_encontrado:
    print("El valor no fue encontrado")
            
            