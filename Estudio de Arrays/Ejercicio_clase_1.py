# colores = ["rojo","verde","amarillo","morado","negro","azul"]
# valor_encontrado = False

# color_a_buscar = input("Ingrese un color: ").lower().strip()
# for indice,color in enumerate(colores):
#     if color == color_a_buscar:
#         print(f"{indice+1}- El color es: {color}")
#         valor_encontrado = True
#         break           
# if not valor_encontrado:
#     print("El valor no fue encontrado")
            
# colores = ["rojo","verde","amarillo"]
# validar_color = False
# validar_existe = False

# while not validar_color:
#     try:
#         color_a_eliminar = input("Ingrese un color: ").strip().lower()
#     except ValueError:
#         print("Ingrese nuevamente")
#     else:
#         validar_color = True
# # colores.append(color_a_buscar)
# while not validar_existe:   

#     try:
#         colores.remove(color_a_eliminar)
#     except ValueError:
#         print("Color no encontrado, intente nuevamente")
#     else:    
#         for indice,color in enumerate(colores):
#             print(f"{indice+1}° el color es: {color}")
#         validar_existe = True


colores = ["rojo","verde","amarillo"]
colores.sort()
for color in colores:
    print(color)