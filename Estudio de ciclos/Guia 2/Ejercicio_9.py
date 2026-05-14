productos = {"Agua": 12, "Tomates": 0, "Pan": 3, "Pate": 50}

for i,v in productos.items(): #i y v se refieren al nombre del producto y a su cantidad, por ejemplo i = "Agua" y v= 12, ocupar el productos.items() hace que recorra todo el diccionario, el producto con el valor
    if v <= 0: #v equivale a la cantidad en stock
        print(f"falta de stock en {i}")
    elif v > 0 and v <= 10:
        print(f"Stock de productos bajo de {i}")
    elif v > 10:
        print(f"El stock de {i} es suficiente")