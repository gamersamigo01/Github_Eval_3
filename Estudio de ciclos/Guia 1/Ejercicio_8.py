pasajes = int(input("¡Cuantos pasajes va a vender?: "))

totalingresos = 0

for i in range(pasajes):
    try:
        costo = int(input("Ingrese el coste del pasaje: "))
        totalingresos = costo + totalingresos
    except ValueError:
        while not costo.isdigit():
            print("Error, Tiene que ser un digito")
            costo = int(input("Ingrese el coste del pasaje: "))
            
            
print(f"El total de las ventas de los pasajes es de: {totalingresos}")