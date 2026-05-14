productos = {"Agua": 12, "Tomates": 0, "Pan": 3, "Pate": 50}

for i,v in productos.items():
    if v <= 0:
        print(f"falta de stock en {i}")
    elif v > 0 and v <= 10:
        print(f"Stock de productos bajo de {i}")
    elif v > 10:
        print(f"El stock de {i} es suficiente")